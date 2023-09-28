from django.shortcuts import render
from .models import Post, Tag
from django.core.paginator import Paginator

# Create your views here.

# Get all posts
def get_posts(tag__name=None, tag__parent_tag__name=None):
    if tag__name is None: # Return all posts if the tag_name parameter is not passed
        posts = Post.objects.all().order_by('-created_at')
    else: # Or filter it
        # Create an empty dictionary to store the filter conditions
        filters = {}

        # Add filter conditions based on the provided parameters
        if tag__name:
            filters['tag__name'] = tag__name
        if tag__parent_tag__name:
            filters['tag__parent_tag__name'] = tag__parent_tag__name

        posts = Post.objects.filter(**filters).order_by('-created_at')
    return posts

# Get all posts with paganation
def get_posts_pagination(request, tag__name=None, tag__parent_tag__name=None):
    data = get_posts(tag__name=tag__name, tag__parent_tag__name=tag__parent_tag__name)
    posts_per_page = 10
    paginator = Paginator(data, posts_per_page)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return posts

def get_recommend_posts(tag__name=None, tag__parent_tag__name=None):
    posts = get_posts(tag__name, tag__parent_tag__name).order_by('-click_count')[:8]
    return posts
    

def get_tags(name=None, parent_tag__name=None):
    if name is None and parent_tag__name is None: # Return all tags if the parameter is not passed
        tags = Tag.objects.all()
    elif name and parent_tag__name is None:
        tags = Tag.objects.get(name=name)
    else: # Or filter it
        # Create an empty dictionary to store the filter conditions
        filters = {}

        # Add filter conditions based on the provided parameters
        if name:
            filters['name'] = name
        if parent_tag__name:
            filters['parent_tag__name'] = parent_tag__name
        
        tags = Tag.objects.filter(**filters).order_by('name')
    return tags
    
# Main page
def index(request):
    posts = get_posts_pagination(request)
    recommend_posts = get_recommend_posts()
    posts_movie = get_posts('Phim Ảnh')[:6]
    posts_video_game = get_posts('Video Game')[:6]
    posts_anime = get_posts('Anime')
    posts_manga = get_posts('Manga')
    posts_music = get_posts('Âm Nhạc')[:6]
    return render(request, 'index.html', {'posts': posts, 'recommend_posts': recommend_posts, 'posts_movie': posts_movie, 'posts_anime': posts_anime, 'posts_manga': posts_manga, 'posts_video_game': posts_video_game, 'posts_music': posts_music})

# All posts page
def posts_all(request):
    posts = get_posts_pagination(request)
    recommend_posts = get_recommend_posts()
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts})

# All review posts page
def posts_review_all(request):
    posts = get_posts_pagination(request, tag__name='Review')
    recommend_posts = get_recommend_posts(tag__name='Review')
    # Custom tag
    tag = {'name': 'Review', 'description': 'Những bài viết review của mình, tất cả đều là đánh giá chủ quan từ bản thân. Lưu ý: Những bài viết đều chứa spoiler, xin hãy cân nhắc trước khi đọc'}
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})

# All thought posts page
def posts_thought_all(request):
    posts = get_posts_pagination(request, tag__name='Cảm Nhận')
    recommend_posts = get_recommend_posts(tag__name='Cảm Nhận')
    # Custom tag
    tag = {'name': 'Cảm nhận', 'description': 'Những bài viết nói lên cảm nhận của mình về những nội dung mình đã thưởng thức. Có những suy nghĩ chi tiết hơn về nội dung đó. Lưu ý: Những bài viết có thể chứa spoiler, xin hãy cân nhắc trước khi đọc'}
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})

# All discuss posts page
def posts_discuss_all(request):
    posts = get_posts_pagination(request, tag__name='Bàn Luận')
    recommend_posts = get_recommend_posts(tag__name='Bàn Luận')
    # Custom tag
    tag = {'name': 'Bàn Luận', 'description': 'Những bài viết review của mình, tất cả đều là đánh giá chủ quan từ bản thân. Lưu ý: Những bài viết đều chứa spoiler, xin hãy cân nhắc trước khi đọc'}
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})

# A post view page
def post_view(request, pk):
    # Retrieve the post based on pk
    post = Post.objects.get(pk=pk)
    # Get the post main tag
    main_tag = post.tag.first()
    # Recommend posts with same tag
    recommend_posts_tag = Post.objects.filter(tag__name=main_tag.name).exclude(pk=pk).order_by('-created_at')[:5]
    # Recommend posts
    recommend_posts = Post.objects.all().exclude(pk=pk).order_by('-created_at')[:5]
    # Count number of words
    time_read = round(post.word_count() / 200)
    # Increase the time post has been seen
    post.increment_click_count()
    return render(request, 'post_view.html', {'post': post, 'main_tag': main_tag, 'recommend_posts_tag': recommend_posts_tag, 'recommend_posts': recommend_posts, 'time_read': time_read})

# About me page
def about_me(request):
    return render(request, 'about-me.html')
    
# Movies
def movies_all(request):
    posts = get_posts_pagination(request, tag__name='Phim Ảnh')
    recommend_posts = get_recommend_posts(tag__name='Phim Ảnh')
    tag = get_tags(name='Phim Ảnh')
    sub_tags = get_tags(parent_tag__name='Phim Ảnh')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag, 'sub_tags': sub_tags})


def movies_review(request):
    posts = get_posts_pagination(request, tag__name='Review', tag__parent_tag__name='Phim Ảnh')
    recommend_posts = get_recommend_posts(tag__name='Review', tag__parent_tag__name='Phim Ảnh')
    tag = Tag.objects.get(name='Review', parent_tag__name='Phim Ảnh')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})


def movies_thought(request):
    posts = get_posts_pagination(request, tag__name='Cảm Nhận', tag__parent_tag__name='Phim Ảnh')
    recommend_posts = get_recommend_posts(tag__name='Cảm Nhận', tag__parent_tag__name='Phim Ảnh')
    tag = Tag.objects.get(name='Cảm Nhận', parent_tag__name='Phim Ảnh')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})


def movies_discuss(request):
    posts = get_posts_pagination(request, tag__name='Bàn Luận', tag__parent_tag__name='Phim Ảnh')
    recommend_posts = get_recommend_posts(tag__name='Bàn Luận', tag__parent_tag__name='Phim Ảnh')
    tag = Tag.objects.get(name='Bàn Luận', parent_tag__name='Phim Ảnh')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})

# Animes
def animes_all(request):
    posts = get_posts_pagination(request, tag__name='Anime')
    recommend_posts = get_recommend_posts(tag__name='Anime')
    tag = get_tags(name='Anime')
    sub_tags = get_tags(parent_tag__name='Anime')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag, 'sub_tags': sub_tags})


def animes_review(request):
    posts = get_posts_pagination(request, tag__name='Review', tag__parent_tag__name='Anime')
    recommend_posts = get_recommend_posts(tag__name='Review', tag__parent_tag__name='Anime')
    tag = Tag.objects.get(name='Review', parent_tag__name='Anime')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})


def animes_thought(request):
    posts = get_posts_pagination(request, tag__name='Cảm Nhận', tag__parent_tag__name='Anime')
    recommend_posts = get_recommend_posts(tag__name='Cảm Nhận', tag__parent_tag__name='Anime')
    tag = Tag.objects.get(name='Cảm Nhận', parent_tag__name='Anime')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})


def animes_discuss(request):
    posts = get_posts_pagination(request, tag__name='Bàn Luận', tag__parent_tag__name='Anime')
    recommend_posts = get_recommend_posts(tag__name='Bàn Luận', tag__parent_tag__name='Anime')
    tag = Tag.objects.get(name='Bàn Luận', parent_tag__name='Anime')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})


# Mangas
def mangas_all(request):
    posts = get_posts_pagination(request, tag__name='Manga')
    recommend_posts = get_recommend_posts(tag__name='Manga')
    tag = get_tags(name='Manga')
    sub_tags = get_tags(parent_tag__name='Manga')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag, 'sub_tags': sub_tags})


def mangas_review(request):
    posts = get_posts_pagination(request, tag__name='Review', tag__parent_tag__name='Manga')
    recommend_posts = get_recommend_posts(tag__name='Review', tag__parent_tag__name='Manga')
    tag = Tag.objects.get(name='Review', parent_tag__name='Manga')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})


def mangas_thought(request):
    posts = get_posts_pagination(request, tag__name='Cảm Nhận', tag__parent_tag__name='Manga')
    recommend_posts = get_recommend_posts(tag__name='Cảm Nhận', tag__parent_tag__name='Manga')
    tag = Tag.objects.get(name='Cảm Nhận', parent_tag__name='Manga')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})

# Video Games
def video_games_all(request):
    posts = get_posts_pagination(request, tag__name='Video Game')
    recommend_posts = get_recommend_posts(tag__name='Video Game')
    tag = get_tags(name='Video Game')
    sub_tags = get_tags(parent_tag__name='Video Game')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag, 'sub_tags': sub_tags})


def video_games_review(request):
    posts = get_posts_pagination(request, tag__name='Review', tag__parent_tag__name='Video Game')
    recommend_posts = get_recommend_posts(tag__name='Review', tag__parent_tag__name='Video Game')
    tag = Tag.objects.get(name='Review', parent_tag__name='Video Game')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})


def video_games_thought(request):
    posts = get_posts_pagination(request, tag__name='Cảm Nhận', tag__parent_tag__name='Video Game')
    recommend_posts = get_recommend_posts(tag__name='Cảm Nhận', tag__parent_tag__name='Video Game')
    tag = Tag.objects.get(name='Cảm Nhận', parent_tag__name='Video Game')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})


# Musics
def musics_all(request):
    posts = get_posts_pagination(request, tag__name='Âm Nhạc')
    recommend_posts = get_recommend_posts(tag__name='Âm Nhạc')
    tag = get_tags(name='Âm Nhạc')
    sub_tags = get_tags(parent_tag__name='Âm Nhạc')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag, 'sub_tags': sub_tags})


def musics_thought(request):
    posts = get_posts_pagination(request, tag__name='Cảm Nhận', tag__parent_tag__name='Âm Nhạc')
    recommend_posts = get_recommend_posts(tag__name='Cảm Nhận', tag__parent_tag__name='Âm Nhạc')
    tag = Tag.objects.get(name='Cảm Nhận', parent_tag__name='Âm Nhạc')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})


def musics_album(request):
    posts = get_posts_pagination(request, tag__name='Album', tag__parent_tag__name='Âm Nhạc')
    recommend_posts = get_recommend_posts(tag__name='Album', tag__parent_tag__name='Âm Nhạc')
    tag = Tag.objects.get(name='Album', parent_tag__name='Âm Nhạc')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})


def musics_song(request):
    posts = get_posts_pagination(request, tag__name='Bài Hát', tag__parent_tag__name='Âm Nhạc')
    recommend_posts = get_recommend_posts(tag__name='Bài Hát', tag__parent_tag__name='Âm Nhạc')
    tag = Tag.objects.get(name='Bài Hát', parent_tag__name='Âm Nhạc')
    return render(request, 'list.html', {'posts': posts, 'recommend_posts': recommend_posts, 'tag': tag})
