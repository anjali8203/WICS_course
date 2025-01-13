import boto3
import logging
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import UploadFileForm, ProjectForm, MessageForm
from allauth.account.views import SignupView
from django.contrib.auth import authenticate, login, get_user_model
from allauth.account.views import LoginView
from .models import UploadedFile, UserProfile, Project, Vote
from django.contrib.auth.models import User, AnonymousUser, Group
from django.conf import settings
from django.core.files.base import File, ContentFile
from django.utils import timezone
from django.contrib.auth import logout, get_backends
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from botocore.exceptions import ClientError
from django.views.decorators.http import require_POST

logger = logging.getLogger(__name__)


class CustomSignUpView(SignupView):
    def form_valid(self, form):
        # Save the new user
        user = form.save(self.request)

        # if not user.groups.exists():
        #     default_group, _ = Group.objects.get_or_create(name='Common User')
        #     user.groups.add(default_group)
        #     user.save()

        # Manually set the backend to avoid multiple backend issues
        backend = get_backends()[0]  # Assuming the first backend is the correct one
        user.backend = f"{backend.__module__}.{backend.__class__.__name__}"

        # Log the user in automatically
        login(self.request, user, backend=user.backend)

        # Redirect to the profile creation page
        return redirect("create_user_profile")


@login_required
def create_user_profile(request):
    if request.method == "POST":
        real_name = request.POST.get("real_name")
        interests = request.POST.get("interests")
        description = request.POST.get("description")

            # Validation: Ensure all required fields are filled
        if not real_name:
            return render(
                request,
                "create_user_profile.html",
                {
                    "user": request.user,
                    "error": "Name is required.",
                },
            )

        # so we can use this later instead of the "username" which is just the email
        request.user.first_name = real_name
        request.user.save()

        # Create the user profile instance and save to the database
        user_profile = UserProfile.objects.create(
            user=request.user,
            real_name=real_name,
            email=request.user.email,
            date_joined=timezone.now(),
            interests=interests,
            description=description,
        )
        user_profile.save()

        return redirect(
            "user_dashboard"
        )  # Redirect to user dashboard after profile creation

    return render(request, "create_user_profile.html", {"user": request.user, "is_pma": is_pma_administrator(request.user)})


def login_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'anonymous':
            return redirect('anonymous_login')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                # Return an 'invalid login' error message.
                return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def anonymous_login(request):
    if not request.session.session_key:
        # Create a new session if it doesn't exist
        request.session.create()
    # Store anonymous-specific data in the session (optional)
    request.session['anonymous_user'] = True
    return redirect('anonymous_project_list')

def anonymous_project_list(request):
    # Fetch project titles and owners only
    projects = Project.objects.all().only('title', 'owner')

    # Pass the data to the template
    return render(request, 'anonymous_project_list.html', {'projects': projects})


# Check if the user is a PMA Administrator based on a hardcoded condition (username/email)
def is_pma_administrator(user):
    return user.groups.filter(name="PMA Admin").exists()

def manage_projects(request):
    projects = Project.objects.all()
    return render(request, 'manage_projects_pma.html', {'projects': projects})

@login_required
def project_details_pma(request, project_id):
    messages.warning(
        request, 
        "PMA Administrators cannot post a message, upload a file, or request to join projects."
    )
    project = get_object_or_404(Project, id=project_id)
    is_pma = is_pma_administrator(request.user)  # Check PMA status
    if not is_pma_administrator(request.user):
        messages.error(request, "You are not authorized to view this page.")
        return redirect('user_dashboard')
    
    return render(request, 'project_detail.html', {'project': project})


# PMA Administrator Dashboard
@login_required
def pma_dashboard(request):
    if not is_pma_administrator(request.user):
        return redirect(
            "user_dashboard"
        )  # If not a PMA Admin, redirect to user dashboard
    return render(request, "pma_dashboard.html", {"is_pma": True})


# @login_required
# def user_dashboard(request):
#     return render(request, "user_dashboard.html", {"is_pma": False})


@login_required
def user_dashboard(request):
    if is_pma_administrator(request.user):
        return redirect("pma_dashboard")
    
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if not user_profile.real_name.strip():  # Check if `real_name` is blank
            return redirect('create_user_profile')
    except UserProfile.DoesNotExist:
        return redirect('create_user_profile')
    # Query projects where the current user is the owner
    owned_projects = Project.objects.filter(owner=request.user)

    # prob also need to show projects where the user is a member
    member_projects = Project.objects.filter(members=request.user).distinct()

    # Prepare the context with both sets of projects
    context = {
        'owned_projects': owned_projects,
        'member_projects': member_projects,
        'is_pma': False,
        'real_name': user_profile.real_name, 
    }

    return render(request, "user_dashboard.html", context)


@login_required
def login_redirect(request):
    is_pma = request.POST.get("pma_checkbox", False)
    is_user = request.POST.get("user_checkbox", False)

    # Redirect based on checkbox selection
    if is_pma and is_pma_administrator(request.user):
        return redirect("pma_dashboard")  # Redirect to PMA dashboard
    elif is_user:
        return redirect("user_dashboard")  # Redirect to User dashboard
    else:
        return redirect("user_dashboard")  # Default to User dashboard


# Custom Login View to handle both checkboxes: PMA and User
class CustomLoginView(LoginView):
    def form_valid(self, form):
        # is_pma = self.request.POST.get(
        #     "pma_checkbox", False
        # )  # Check if PMA Administrator is checked
        # is_user = self.request.POST.get(
        #     "user_checkbox", False
        # )  # Check if User is checked

        # Log in the user
        login(self.request, form.user)

        # Check if the user has a profile
        try:
            user_profile = UserProfile.objects.get(user=form.user)
        except UserProfile.DoesNotExist:
            # Redirect to profile creation if the profile does not exist
            return redirect('create_user_profile')

        # If 'next' parameter exists, respect it
        next_url = self.request.GET.get("next")
        if next_url:
            return redirect(next_url)

        # If PMA checkbox is selected
        if is_pma_administrator(self.request.user):
            return redirect("pma_dashboard")

        # If neither checkbox is selected
        else:
            # Redirect to login with an error message or default to user_dashboard
            return redirect("user_dashboard")


def upload_file_to_s3(file, bucket_name, object_name=None, metadata=None):
    s3_client = boto3.client("s3")

    if object_name is None:
        object_name = file.name

    content_type = (
        file.content_type if file.content_type else "application/octet-stream"
    )

    extra_args = {"ContentType": content_type}
    if metadata:
        extra_args["Metadata"] = metadata  # Add metadata if provided

    try:
        print(f"Uploading file: {file}")
        print(f"Bucket: {bucket_name}")
        print(f"Object Name: {object_name}")
        print(f"Content Type: {content_type}")

        s3_client.upload_fileobj(
            Fileobj=file, Bucket=bucket_name, Key=object_name, ExtraArgs=extra_args
        )
        logger.info(f"File {object_name} uploaded successfully to {bucket_name}")
        return True
    except Exception as e:
        logger.error(f"Failed to upload {object_name} to {bucket_name}: {str(e)}")
        print(f"Error during S3 upload: {e}")
        return False

@login_required
def view_profile(request):
    try:
        # Retrieve the user's profile
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If profile does not exist, redirect to profile creation
        return redirect("create_user_profile")

    return render(request, "view_profile.html", {"profile": user_profile, "is_pma": is_pma_administrator(request.user)})

@login_required
def file_upload(request, project_id):
    if is_pma_administrator(request.user):
        messages.error(request, "PMA Administrators cannot upload files.")
        return redirect('project_detail', project_id=project_id)
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES.get("file")
            title = request.POST.get("title")
            description = request.POST.get("description")
            keywords = request.POST.get("keywords")

            if not file:
                messages.error(request, "No file to upload.")
                return redirect('project_file_upload', project_id=project_id)

            bucket_name = "project-b-13-bucket"
            object_name = file.name

            # Prepare optional metadata
            metadata = {'title': title, 'description': description, 'keywords': keywords}

            # Upload file to S3 with optional metadata
            success = upload_file_to_s3(file, bucket_name, object_name, metadata)
            if success:
                uploaded_file = UploadedFile(
                    project=project,
                    author=request.user,
                    s3_url=f"https://{bucket_name}.s3.amazonaws.com/{object_name}",
                    file_mime=file.content_type,
                    file_type=file.content_type.split("/")[-1]
                    if file.content_type
                    else "unknown",
                    title=title,
                    description=description,
                    keywords=keywords,
                )

                uploaded_file.file.name = object_name
                uploaded_file.save()

                messages.success(request, "File uploaded successfully.")
                return redirect('project_detail', project_id=project_id)  # Redirect to project detail page
            else:
                messages.error(request, "Upload failed.")
                return redirect('project_file_upload', project_id=project_id)
        else:
            messages.error(request, "Invalid form.")
            return render(request, 'upload.html', {'form': form, 'project': project})
    else:
        form = UploadFileForm()
        return render(request, "upload.html", {"form": form, "project": project})
    

@login_required
def your_projects(request):
    """
    View to display projects that the user owns or authored.
    """
    # Fetch projects owned by the user
    projects = Project.objects.filter(owner=request.user)
    user_votes = Vote.objects.filter(user=request.user)
    vote_dict = {vote.project.id: vote.vote_type for vote in user_votes}

    # apparently this 'user_vote' is a temporary field
    for project in projects:
        project.user_vote = vote_dict.get(project.id, None)

    return render(request, "your_projects.html", {"projects": projects})

@login_required
def joined_projects(request):
    """
    View to display projects that the user has joined as a member.
    """
    projects = Project.objects.filter(members=request.user).exclude(owner=request.user)
    user_votes = Vote.objects.filter(user=request.user)
    vote_dict = {vote.project.id: vote.vote_type for vote in user_votes}

    # apparently this 'user_vote' is a temporary field
    for project in projects:
        project.user_vote = vote_dict.get(project.id, None)

    return render(request, "projects_list.html", {"projects": projects})


def landing_page(request):
    if request.user.is_authenticated:  # Check if the user is logged in
        return redirect("user_dashboard")  # Redirect to the user dashboard
    return render(request, "landing_page.html")

# view_all_member_projs
def view_all_member_projs(request):
    projects = Project.objects.all().only("title", "owner", "description", "creation_date")
    is_pma = {"is_pma": False, "files": UploadedFile.objects.all()}
    if request.user.is_authenticated:
        is_pma["is_pma"] = is_pma_administrator(request.user)
    return render(request, "view_all_member_projs.html", is_pma)


def s3_delete(request, file):
    try:
        logger.info(f"Attempting to delete file {file.title}")
        
        # Delete from S3
        s3_client = boto3.client('s3')
        if file.file and file.file.name:
            logger.info(f"Deleting file {file.file.name} from S3 bucket {settings.AWS_STORAGE_BUCKET_NAME}")
            try:
                print(f"Bucket: project-b-13-bucket, Key: {file.file.name}")
                response = s3_client.delete_object(Bucket= 'project-b-13-bucket', Key=file.file.name)
                print(f"S3 Delete Response: {response}")
                logger.info(f"Successfully deleted file from S3")
            except Exception as e:
                logger.error(f"Error deleting file from S3: {str(e)}")
                raise 
        else:
            logger.warning(f"File {file.title} has no associated S3 object name")
            messages.warning(request, "No associated S3 object name found.")

        # Delete from database
        logger.info(f"Deleting file record {file.title} from database")
        file.delete()
        logger.info(f"Successfully deleted file record from database")

        messages.success(request, f"File '{file.title}' has been deleted.")
    except Exception as e:
        logger.error(f"Unexpected error during file deletion: {str(e)}", exc_info=True)
        messages.error(request, f"An unexpected error occurred while deleting the file: {str(e)}")


@login_required
def delete_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    next = request.POST.get('next', '/') # now working I think
    if request.method == 'POST':
        s3_delete(request, file)
    return HttpResponseRedirect(next)


#travel guide information for user 
def travel_guide(request):
    return render(request, 'travel_guide.html')

def logout_view(request):
    logout(request)  # This logs the user out
    # Redirect to home page or render a custom template
    return render(request, 'account/sign_out.html')

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.owner = request.user  # Setting the owner to the current user
            new_project.save()
            form.save_m2m()  # Save many-to-many relationships if applicable
            return redirect('user_dashboard')  # Redirect to dashboard or project detail
        else:
            return render(request, 'create_project.html', {'form': form})
    else:
        form = ProjectForm()
        return render(request, 'create_project.html', {'form': form})


@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_details.html', {'project': project})

@login_required
def add_member_to_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        project.members.add(user)
        messages.success(request, "Member added successfully.")
        return redirect('project_detail', project_id=project_id)
    users = User.objects.exclude(id__in=project.members.all())
    return render(request, 'add_member.html', {'project': project, 'users': users})

@login_required
def post_project_message(request, project_id):
    if is_pma_administrator(request.user):
        messages.error(request, "PMA Administrators cannot post messages.")
        return redirect('project_detail', project_id=project_id)
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.author = request.user
            new_message.project = project
            new_message.save()
            messages.success(request, "Message posted successfully.")
            return redirect('project_detail', project_id=project_id)
    else:
        form = MessageForm()
    return render(request, 'post_message.html', {'form': form, 'project': project})


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects_list.html', {'projects': projects})

@require_POST
def vote(request):
    try:
        data = json.loads(request.body)
        project_id = data.get("project_id")
        vote_type = data.get("vote_type")
        project = get_object_or_404(Project, id=project_id)


        if vote_type == 'up' or vote_type == 'clear_down_up':
            Vote.objects.update_or_create(**{"user": request.user, "project": project}, defaults={"vote_type": 1})
        elif vote_type == 'down' or vote_type == 'clear_up_down':
            Vote.objects.update_or_create(**{"user": request.user, "project": project}, defaults={"vote_type": -1})
        else:
            Vote.objects.update_or_create(**{"user": request.user, "project": project}, defaults={"vote_type": 0})

        # have to redo these conditions since one button can be pressed while the other is still 'active'
        if vote_type == 'up' or vote_type == 'clear_down':
            project.votes += 1  
        elif vote_type == 'down' or vote_type == 'clear_up':
            project.votes -= 1
        elif vote_type == 'clear_down_up':
            project.votes += 2
        elif vote_type == 'clear_up_down':
            project.votes -= 2
        project.save()  


        return JsonResponse({'success': True, 'votes': project.votes}) 
    except Exception as e:
        return JsonResponse({'success': False}) 

@login_required
def delete_project(request, project_id): 
    # Fetch the project object
    project = get_object_or_404(Project, id=project_id)
    # Check if the current user is the owner or a PMA admin
    if project.owner != request.user and not is_pma_administrator(request.user):
        messages.error(request, "You are not authorized to delete this project.")
        return redirect('project_detail', project_id=project_id)

    if request.method == "POST":
        # delete all files in the project as well
        files = UploadedFile.objects.filter(project=project)
        for file in files:
            s3_delete(request, file)

        # Delete the project
        project.delete()
        messages.success(request, "Project deleted successfully.")
        return redirect('user_dashboard')

    # Render a confirmation page before deletion
    return render(request, "deleteProjectConfirm.html", {"project": project})

@login_required
def request_to_join(request, project_id):
    if is_pma_administrator(request.user):
        messages.error(request, "PMA Administrators cannot join projects.")
        return redirect('explore_projects')
    
    project = get_object_or_404(Project, id=project_id)
    
    # Check if the user is already a member or has already requested
    if project.members.filter(id=request.user.id).exists():
        messages.warning(request, "You are already a member of this project.")
    elif JoinRequest.objects.filter(project=project, user=request.user).exists():
        messages.warning(request, "You have already requested to join this project.")
    else:
        # Create a join request
        JoinRequest.objects.create(project=project, user=request.user)
        messages.success(request, "Your request to join has been sent.")
    
    return redirect('explore_projects')

@login_required
def manage_requests(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Only the owner can view this
    if project.owner != request.user:
        messages.error(request, "You are not authorized to manage requests for this project.")
        return redirect('project_detail', project_id=project_id)
    
    requests = project.join_requests.all()

    if request.method == "POST":
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')

        if action == 'accept':
            user = get_object_or_404(User, id=user_id)
            project.members.add(user)
            JoinRequest.objects.filter(project=project, user=user).delete()
            messages.success(request, f"{user.username} has been added to the project.")
        elif action == 'decline':
            JoinRequest.objects.filter(project=project, user_id=user_id).delete()
            messages.info(request, "Request has been declined.")
    
    return render(request, 'manage_requests.html', {'project': project, 'requests': requests})

@login_required
def leave_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Ensure the user is a member
    if not project.members.filter(id=request.user.id).exists():
        messages.error(request, "You are not a member of this project.")
    else:
        project.members.remove(request.user)
        messages.success(request, "You have left the project.")

    return redirect('user_dashboard')  # Redirect to the user's dashboard or profile

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project, JoinRequest

@login_required
def manage_requests(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Ensure only the project owner can manage requests
    if request.user != project.owner:
        messages.error(request, "You are not authorized to manage requests for this project.")
        return redirect('project_detail', project_id=project.id)

    if request.method == "POST":
        user_id = request.POST.get("user_id")
        action = request.POST.get("action")
        join_request = get_object_or_404(JoinRequest, project=project, user_id=user_id)

        if action == "accept":
            project.members.add(join_request.user)
            join_request.delete()
            messages.success(request, f"{join_request.user.username} has been added to the project.")
        elif action == "decline":
            join_request.delete()
            messages.info(request, f"{join_request.user.username}'s request has been declined.")

        return redirect('manage_requests', project_id=project.id)

    requests = JoinRequest.objects.filter(project=project)
    return render(request, 'manage_requests.html', {'project': project, 'requests': requests})

@login_required
def explore_projects(request):
    """
    View to display all available projects, highlighting if the user is a member or owner.
    """
    # projects = Project.objects.all()
    # project_list = []

    # for project in projects:
    #     is_member = project.members.filter(id=request.user.id).exists()
    #     is_owner = project.owner == request.user
    #     project_list.append({
    #         "project": project,
    #         "is_member": is_member,
    #         "is_owner": is_owner,
    #     })

    # return render(request, 'explore_projects.html', {
    #     'project_list': project_list,
    # })
    projects = Project.objects.exclude(members=request.user).exclude(owner=request.user).only('title', 'owner')
    return render(request, 'explore_projects.html', {'projects': projects})




    