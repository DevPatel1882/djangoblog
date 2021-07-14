from django.shortcuts import render,redirect
from info_data.models import Blog_Post
from info_data.models import Contact_us
from info_data.models import Funny_Images
from info_data.models import Viral_Video
from django.core.paginator import Paginator
from info_data.models import Feedback
from info_data.models import Leave_a_Reply



def master(request):
    CAR_NEWS = Blog_Post.objects.filter(Category='CAR_NEWS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    ENTERTAINMENT = Blog_Post.objects.filter(Category='ENTERTAINMENT',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    GEDGETS = Blog_Post.objects.filter(Category='GEDGETS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    TRAVEL = Blog_Post.objects.filter(Category='TRAVEL',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    WORLDWIDE = Blog_Post.objects.filter(Category='WORLDWIDE',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]

    POST = Blog_Post.objects.filter(Published=True).order_by('-id')
    context = {
               'POST':POST,
               'CAR_NEWS':CAR_NEWS,
               'ENTERTAINMENT':ENTERTAINMENT,
               'GEDGETS':GEDGETS,
               'TRAVEL':TRAVEL,
               'WORLDWIDE':WORLDWIDE,

              }

    #gadgets_nav = GADGETS_Info.objects.filter(Published=True).order_by('-id')[0:4]
    return render(request,'master.html',context)


def index(request):
    # FEEDBACK FORM POST REQUEST
    if request.method == "POST":
        feedback = request.POST['feedback']
        Short_Summery = request.POST['Short_Summery']
        email = request.POST['email']
        ins = Feedback(feedback=feedback, Short_Summery=Short_Summery, email=email)
        ins.save()
    # NAVIGATION IN NEWS CATEGORY WISE SHOW
    CAR_NEWS = Blog_Post.objects.filter(Category='CAR_NEWS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    ENTERTAINMENT = Blog_Post.objects.filter(Category='ENTERTAINMENT',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    GEDGETS = Blog_Post.objects.filter(Category='GEDGETS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    TRAVEL = Blog_Post.objects.filter(Category='TRAVEL',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    WORLDWIDE = Blog_Post.objects.filter(Category='WORLDWIDE',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]

    # PAGINATATION CODEING
    POST = Blog_Post.objects.filter(Published=True).order_by('-id')
    paginator = Paginator(POST, 6)
    page_number = request.GET.get('page')
    POST_obj = paginator.get_page(page_number)

    # ASIDE FUNCTIONS
    VIDEO = Viral_Video.objects.filter(Aside_Show=True,Published=True).order_by('-id')[0:1]
    ASIDE_POPULAR_POSTS = Blog_Post.objects.filter(Aside_Show=True,Published=True).order_by('-id')[0:4]
    ASIDE_POPULAR_GEDGETS = Blog_Post.objects.filter(Aside_Show=True,Category='GEDGETS',Published=True).order_by('-id')[0:4]
    FUNNY_IMG = Funny_Images.objects.filter(Aside_Show=True, Published=True).order_by('-id')[0:1]

    context = {
        'POST': POST_obj,
        'CAR_NEWS': CAR_NEWS,
        'ENTERTAINMENT': ENTERTAINMENT,
        'GEDGETS': GEDGETS,
        'TRAVEL': TRAVEL,
        'WORLDWIDE': WORLDWIDE,
        'VIDEO':VIDEO,
        'ASIDE_POPULAR_POSTS':ASIDE_POPULAR_POSTS,
        'ASIDE_POPULAR_GEDGETS':ASIDE_POPULAR_GEDGETS,
        'FUNNY_IMG': FUNNY_IMG,
    }
    return render(request, 'index.html', context)


def contact(request):
    CAR_NEWS = Blog_Post.objects.filter(Category='CAR_NEWS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    ENTERTAINMENT = Blog_Post.objects.filter(Category='ENTERTAINMENT',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    GEDGETS = Blog_Post.objects.filter(Category='GEDGETS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    TRAVEL = Blog_Post.objects.filter(Category='TRAVEL',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    WORLDWIDE = Blog_Post.objects.filter(Category='WORLDWIDE',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    # ASIDE FUNCTIONS
    VIDEO = Viral_Video.objects.filter(Aside_Show=True,Published=True).order_by('-id')[0:1]
    ASIDE_POPULAR_POSTS = Blog_Post.objects.filter(Aside_Show=True,Published=True).order_by('-id')[0:4]
    ASIDE_POPULAR_GEDGETS = Blog_Post.objects.filter(Aside_Show=True, Category='GEDGETS',Published=True).order_by('-id')[0:4]
    FUNNY_IMG = Funny_Images.objects.filter(Aside_Show=True, Published=True).order_by('-id')[0:1]

    context = {
        'CAR_NEWS': CAR_NEWS,
        'ENTERTAINMENT': ENTERTAINMENT,
        'GEDGETS': GEDGETS,
        'TRAVEL': TRAVEL,
        'WORLDWIDE': WORLDWIDE,
        'VIDEO': VIDEO,
        'ASIDE_POPULAR_POSTS': ASIDE_POPULAR_POSTS,
        'ASIDE_POPULAR_GEDGETS': ASIDE_POPULAR_GEDGETS,
        'FUNNY_IMG': FUNNY_IMG,
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contacts = Contact_us(name=name,email=email,subject=subject,message=message)
        contacts.save()
        return render(request,'contact.html',context)
    else:
        return render(request,'contact.html',context)


def Blog(request):
    # NAVIGATION IN NEWS CATEGORY WISE SHOW
    CAR_NEWS = Blog_Post.objects.filter(Category='CAR_NEWS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    ENTERTAINMENT = Blog_Post.objects.filter(Category='ENTERTAINMENT',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    GEDGETS = Blog_Post.objects.filter(Category='GEDGETS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    TRAVEL = Blog_Post.objects.filter(Category='TRAVEL',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    WORLDWIDE = Blog_Post.objects.filter(Category='WORLDWIDE',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]

    # PAGINATATION CODEING
    POST = Blog_Post.objects.filter(Published=True).order_by('-id')
    paginator = Paginator(POST, 6)
    page_number = request.GET.get('page')
    POST_obj = paginator.get_page(page_number)

    # ASIDE FUNCTIONS
    VIDEO = Viral_Video.objects.filter(Aside_Show=True,Published=True).order_by('-id')[0:1]
    ASIDE_POPULAR_POSTS = Blog_Post.objects.filter(Aside_Show=True,Published=True).order_by('-id')[0:4]
    ASIDE_POPULAR_GEDGETS = Blog_Post.objects.filter(Aside_Show=True, Category='GEDGETS',Published=True).order_by('-id')[0:4]
    FUNNY_IMG = Funny_Images.objects.filter(Aside_Show=True, Published=True).order_by('-id')[0:1]

    context = {
        'POST': POST_obj,
        'CAR_NEWS': CAR_NEWS,
        'ENTERTAINMENT': ENTERTAINMENT,
        'GEDGETS': GEDGETS,
        'TRAVEL': TRAVEL,
        'WORLDWIDE': WORLDWIDE,
        'VIDEO': VIDEO,
        'ASIDE_POPULAR_POSTS': ASIDE_POPULAR_POSTS,
        'ASIDE_POPULAR_GEDGETS': ASIDE_POPULAR_GEDGETS,
        'FUNNY_IMG': FUNNY_IMG,
    }
    return render(request,'blog.html',context)





def viral_videos(request):
    viral_videos = Viral_Video.objects.filter(Published=True).order_by('-id')
    # PAGINATHION FUNCTIONS
    paginator = Paginator(viral_videos, 6)
    page_number = request.GET.get('page')
    viral_videos_obj = paginator.get_page(page_number)

    # NAVIGATION IN NEWS CATEGORY WISE SHOW
    CAR_NEWS = Blog_Post.objects.filter(Category='CAR_NEWS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    ENTERTAINMENT = Blog_Post.objects.filter(Category='ENTERTAINMENT',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    GEDGETS = Blog_Post.objects.filter(Category='GEDGETS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    TRAVEL = Blog_Post.objects.filter(Category='TRAVEL',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    WORLDWIDE = Blog_Post.objects.filter(Category='WORLDWIDE',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]

    # ASIDE FUNCTIONS
    VIDEO = Viral_Video.objects.filter(Aside_Show=True,Published=True).order_by('-id')[0:1]
    ASIDE_POPULAR_POSTS = Blog_Post.objects.filter(Aside_Show=True,Published=True).order_by('-id')[0:4]
    ASIDE_POPULAR_GEDGETS = Blog_Post.objects.filter(Aside_Show=True, Category='GEDGETS',Published=True).order_by('-id')[0:4]
    FUNNY_IMG = Funny_Images.objects.filter(Aside_Show=True, Published=True).order_by('-id')[0:1]

    context = {'viral_videos':viral_videos_obj,
               'CAR_NEWS': CAR_NEWS,
               'ENTERTAINMENT': ENTERTAINMENT,
               'GEDGETS': GEDGETS,
               'TRAVEL': TRAVEL,
               'WORLDWIDE': WORLDWIDE,
               'VIDEO': VIDEO,
               'ASIDE_POPULAR_POSTS': ASIDE_POPULAR_POSTS,
               'ASIDE_POPULAR_GEDGETS': ASIDE_POPULAR_GEDGETS,
               'FUNNY_IMG': FUNNY_IMG,
               }
    return render(request,'Blog_videos.html',context)


def funny_images(request):
    funny_img = Funny_Images.objects.filter(Published=True).order_by('-id')

    # NAVIGATION IN NEWS CATEGORY WISE SHOW
    CAR_NEWS = Blog_Post.objects.filter(Category='CAR_NEWS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    ENTERTAINMENT = Blog_Post.objects.filter(Category='ENTERTAINMENT',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    GEDGETS = Blog_Post.objects.filter(Category='GEDGETS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    TRAVEL = Blog_Post.objects.filter(Category='TRAVEL',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    WORLDWIDE = Blog_Post.objects.filter(Category='WORLDWIDE',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]

    # ASIDE FUNCTIONS
    VIDEO = Viral_Video.objects.filter(Aside_Show=True,Published=True).order_by('-id')[0:1]
    ASIDE_POPULAR_POSTS = Blog_Post.objects.filter(Aside_Show=True,Published=True).order_by('-id')[0:4]
    ASIDE_POPULAR_GEDGETS = Blog_Post.objects.filter(Aside_Show=True, Category='GEDGETS',Published=True).order_by('-id')[0:4]
    FUNNY_IMG = Funny_Images.objects.filter(Aside_Show=True,Published=True).order_by('-id')[0:1]

    context = {
                'CAR_NEWS': CAR_NEWS,
                'ENTERTAINMENT': ENTERTAINMENT,
                'GEDGETS': GEDGETS,
                'TRAVEL': TRAVEL,
                'WORLDWIDE': WORLDWIDE,
                'VIDEO': VIDEO,
                'ASIDE_POPULAR_POSTS': ASIDE_POPULAR_POSTS,
                'ASIDE_POPULAR_GEDGETS': ASIDE_POPULAR_GEDGETS,
                'funny_img':funny_img,
                 'FUNNY_IMG': FUNNY_IMG,
               }
    return render(request,'funny_imges.html',context)


def gedgets(request):
    # NAVIGATION IN NEWS CATEGORY WISE SHOW
    CAR_NEWS = Blog_Post.objects.filter(Category='CAR_NEWS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    ENTERTAINMENT = Blog_Post.objects.filter(Category='ENTERTAINMENT',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    GEDGETS = Blog_Post.objects.filter(Category='GEDGETS',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    TRAVEL = Blog_Post.objects.filter(Category='TRAVEL',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    WORLDWIDE = Blog_Post.objects.filter(Category='WORLDWIDE',Published=True,Show_In_Navigation=True).order_by('-id')[0:4]

    # PAGINATATION CODEING
    POST = Blog_Post.objects.filter(Published=True).order_by('-id')
    paginator = Paginator(POST, 6)
    page_number = request.GET.get('page')
    POST_obj = paginator.get_page(page_number)

    # ASIDE FUNCTIONS
    VIDEO = Viral_Video.objects.filter(Aside_Show=True,Published=True).order_by('-id')[0:1]
    ASIDE_POPULAR_POSTS = Blog_Post.objects.filter(Aside_Show=True,Published=True).order_by('-id')[0:4]
    ASIDE_POPULAR_GEDGETS = Blog_Post.objects.filter(Aside_Show=True,Category='GEDGETS',Published=True).order_by('-id')[0:4]
    FUNNY_IMG = Funny_Images.objects.filter(Aside_Show=True, Published=True).order_by('-id')[0:1]


    context = {
        'POST': POST_obj,
        'CAR_NEWS': CAR_NEWS,
        'ENTERTAINMENT': ENTERTAINMENT,
        'GEDGETS': GEDGETS,
        'TRAVEL': TRAVEL,
        'WORLDWIDE': WORLDWIDE,
        'VIDEO': VIDEO,
        'ASIDE_POPULAR_POSTS': ASIDE_POPULAR_POSTS,
        'ASIDE_POPULAR_GEDGETS': ASIDE_POPULAR_GEDGETS,
        'FUNNY_IMG': FUNNY_IMG,
    }
    return render(request,'Gedgets.html',context)




def Blog_single(request,slug):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
        comment = request.POST['comment']
        leave_reply = Leave_a_Reply(name=name,email=email,website=website,comment=comment)
        leave_reply.save()
    else:
        pass
    # Blog Data Show In Title Wise
    POST = Blog_Post.objects.filter(slug=slug)
    if POST.exists():
        POST = POST.first()
    else:
        return redirect('404')

    # NAVIGATION IN NEWS CATEGORY WISE SHOW
    CAR_NEWS = Blog_Post.objects.filter(Category='CAR_NEWS', Published=True, Show_In_Navigation=True).order_by('-id')[0:4]
    ENTERTAINMENT = Blog_Post.objects.filter(Category='ENTERTAINMENT', Published=True,Show_In_Navigation=True).order_by('-id')[0:4]
    GEDGETS = Blog_Post.objects.filter(Category='GEDGETS', Published=True, Show_In_Navigation=True).order_by('-id')[0:4]
    TRAVEL = Blog_Post.objects.filter(Category='TRAVEL', Published=True, Show_In_Navigation=True).order_by('-id')[0:4]
    WORLDWIDE = Blog_Post.objects.filter(Category='WORLDWIDE', Published=True, Show_In_Navigation=True).order_by('-id')[0:4]

    # ASIDE FUNCTIONS
    VIDEO = Viral_Video.objects.filter(Aside_Show=True, Published=True).order_by('-id')[0:1]
    ASIDE_POPULAR_POSTS = Blog_Post.objects.filter(Aside_Show=True, Published=True).order_by('-id')[0:4]
    ASIDE_POPULAR_GEDGETS = Blog_Post.objects.filter(Aside_Show=True, Category='GEDGETS', Published=True).order_by('-id')[0:4]
    FUNNY_IMG = Funny_Images.objects.filter(Aside_Show=True, Published=True).order_by('-id')[0:1]

    context = {
              'CAR_NEWS':CAR_NEWS,
              'ENTERTAINMENT':ENTERTAINMENT,
              'GEDGETS':GEDGETS,
              'TRAVEL':TRAVEL,
              'WORLDWIDE':WORLDWIDE,
              'VIDEO':VIDEO,
              'ASIDE_POPULAR_POSTS':ASIDE_POPULAR_POSTS,
              'ASIDE_POPULAR_GEDGETS':ASIDE_POPULAR_GEDGETS,
              'POST':POST,
              'FUNNY_IMG':FUNNY_IMG,
              }


    return render(request,'single_blog.html',context)


def Error_Page(request):
    return render(request,'404.html')

