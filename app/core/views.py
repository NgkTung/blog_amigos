from django.shortcuts import render
from .models import Post, Tag
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-created_at')
    posts_movie = Post.objects.filter(
        tag__name='Phim Ảnh').order_by('-created_at')
    posts_anime = Post.objects.filter(
        tag__name='Anime').order_by('-created_at')
    posts_manga = Post.objects.filter(
        tag__name='Manga').order_by('-created_at')
    posts_video_game = Post.objects.filter(
        tag__name='Video Game').order_by('-created_at')
    posts_music = Post.objects.filter(
        tag__name='Âm Nhạc').order_by('-created_at')
    return render(request, 'index.html', {'posts': posts, 'posts_movie': posts_movie, 'posts_anime': posts_anime, 'posts_manga': posts_manga, 'posts_video_game': posts_video_game, 'posts_music': posts_music})


def posts_all(request):
    data = Post.objects.all().order_by('-created_at')

    posts_per_page = 10
    paginator = Paginator(data, posts_per_page)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'list.html', {'posts': posts})


def posts_review_all(request):
    posts = Post.objects.filter(tag__name='Review').order_by('-created_at')
    tag = {'name': 'Review', 'description': 'Những bài viết review của mình, tất cả đều là đánh giá chủ quan từ bản thân. Lưu ý: Những bài viết đều chứa spoiler, xin hãy cân nhắc trước khi đọc'}
    return render(request, 'list.html', {'posts': posts, 'tag': tag})


def posts_thought_all(request):
    posts = Post.objects.filter(tag__name='Cảm Nhận').order_by('-created_at')
    tag = {'name': 'Cảm nhận', 'description': 'Những bài viết nói lên cảm nhận của mình về những nội dung mình đã thưởng thức. Có những suy nghĩ chi tiết hơn về nội dung đó. Lưu ý: Những bài viết có thể chứa spoiler, xin hãy cân nhắc trước khi đọc'}
    return render(request, 'list.html', {'posts': posts, 'tag': tag})


def posts_critique_all(request):
    posts = Post.objects.filter(tag__name='Phê Bình').order_by('-created_at')
    tag = {'name': 'Phê Bình', 'description': 'Những bài viết review của mình, tất cả đều là đánh giá chủ quan từ bản thân. Lưu ý: Những bài viết đều chứa spoiler, xin hãy cân nhắc trước khi đọc'}
    return render(request, 'list.html', {'posts': posts, 'tag': tag})


def post_view(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_view.html', {'post': post})

# About me page


def about_me(request):
    return render(request, 'about-me.html')

# Movies


def movies_all(request):
    posts = Post.objects.filter(tag__name='Phim Ảnh').order_by('-created_at')
    tag = Tag.objects.get(name='Phim Ảnh')
    sub_tags = Tag.objects.filter(parent_tag__name='Phim Ảnh')
    return render(request, 'list.html', {'posts': posts, 'tag': tag, 'sub_tags': sub_tags})


def movies_review(request):
    posts = Post.objects.filter(
        tag__name='Review', tag__parent_tag__name='Phim Ảnh').order_by('-created_at')
    tag = Tag.objects.get(
        parent_tag__name='Phim Ảnh', name='Review')
    return render(request, 'list.html', {'posts': posts, 'tag': tag})


def movies_thought(request):
    posts = Post.objects.filter(
        tag__name='Cảm Nhận', tag__parent_tag__name='Phim Ảnh').order_by('-created_at')
    tag = Tag.objects.get(
        parent_tag__name='Phim Ảnh', name='Cảm Nhận')
    return render(request, 'list.html', {'posts': posts, 'tag': tag})


def movies_discuss(request):
    posts = Post.objects.filter(
        tag__name='Bàn Luận', tag__parent_tag__name='Phim Ảnh').order_by('-created_at')
    tag = Tag.objects.get(
        parent_tag__name='Phim Ảnh', name='Bàn Luận')
    return render(request, 'list.html', {'posts': posts, 'tag': tag})

# Animes


def animes_all(request):
    posts = Post.objects.filter(tag__name='Anime').order_by('-created_at')
    tag = Tag.objects.get(name='Anime')
    sub_tags = Tag.objects.filter(parent_tag__name='Anime')
    return render(request, 'list.html', {'posts': posts, 'tag': tag, 'sub_tags': sub_tags})


def animes_review(request):
    posts = Post.objects.filter(
        tag__name='Review', tag__parent_tag__name='Anime').order_by('-created_at')
    tag = Tag.objects.get(
        parent_tag__name='Anime', name='Review')
    return render(request, 'list.html', {'posts': posts, 'tag': tag})


def animes_thought(request):
    posts = Post.objects.filter(
        tag__name='Cảm Nhận', tag__parent_tag__name='Anime').order_by('-created_at')
    tag = Tag.objects.get(
        parent_tag__name='Anime', name='Cảm Nhận')
    return render(request, 'list.html', {'posts': posts, 'tag': tag})


def animes_discuss(request):
    posts = Post.objects.filter(
        tag__name='Bàn Luận', tag__parent_tag__name='Anime').order_by('-created_at')
    tag = Tag.objects.get(
        parent_tag__name='Anime', name='Bàn Luận')
    return render(request, 'list.html', {'posts': posts, 'tag': tag})


# Mangas


def mangas_all(request):
    posts = Post.objects.filter(tag__name='Manga').order_by('-created_at')
    tag = Tag.objects.get(name='Manga')
    sub_tags = Tag.objects.filter(parent_tag__name='Manga')
    return render(request, 'list.html', {'posts': posts, 'tag': tag, 'sub_tags': sub_tags})


def mangas_review(request):
    posts = Post.objects.filter(
        tag__name='Review', tag__parent_tag__name='Manga').order_by('-created_at')
    tag = Tag.objects.get(
        parent_tag__name='Manga', name='Review')
    return render(request, 'list.html', {'posts': posts, 'tag': tag})


def mangas_thought(request):
    posts = Post.objects.filter(
        tag__name='Cảm Nhận', tag__parent_tag__name='Manga').order_by('-created_at')
    tag = Tag.objects.get(
        parent_tag__name='Manga', name='Cảm Nhận')
    return render(request, 'list.html', {'posts': posts, 'tag': tag})

# Video Games


def video_games_all(request):
    posts = Post.objects.filter(tag__name='Video Game').order_by('-created_at')
    tag = Tag.objects.get(name='Video Game')
    sub_tags = Tag.objects.filter(parent_tag__name='Video Game')
    return render(request, 'list.html', {'posts': posts, 'tag': tag, 'sub_tags': sub_tags})


def video_games_review(request):
    posts = Post.objects.filter(
        tag__name='Review', tag__parent_tag__name='Video Game').order_by('-created_at')
    tag = Tag.objects.get(
        parent_tag__name='Video Game', name='Review')
    return render(request, 'list.html', {'posts': posts, 'tag': tag})


def video_games_thought(request):
    posts = Post.objects.filter(
        tag__name='Cảm Nhận', tag__parent_tag__name='Video Game').order_by('-created_at')
    tag = Tag.objects.get(
        parent_tag__name='Video Game', name='Cảm Nhận')
    return render(request, 'list.html', {'posts': posts, 'tag': tag})


# Musics

def musics_all(request):
    posts = Post.objects.filter(tag__name='Âm Nhạc').order_by('-created_at')
    tag = Tag.objects.get(name='Âm Nhạc')
    sub_tags = Tag.objects.filter(parent_tag__name='Âm Nhạc')
    return render(request, 'list.html', {'posts': posts, 'tag': tag, 'sub_tags': sub_tags})
