from django.urls import path
from .views import index, post_view, about_me, posts_all, movies_all, movies_review, movies_thought, movies_discuss, animes_all, animes_review, animes_thought, animes_discuss, video_games_all, video_games_review, video_games_thought, mangas_all, mangas_review, mangas_thought, musics_all, musics_thought, musics_album, musics_song, posts_review_all, posts_thought_all, posts_critique_all

urlpatterns = [
    # Home page
    path('', index, name='index'),
    # All posts page
    path('posts/', posts_all, name='posts'),
    path('posts/review', posts_review_all, name='posts_review'),
    path('posts/thought', posts_thought_all, name='posts_thought'),
    path('posts/critique', posts_critique_all, name='posts_critique'),
    # Movie pages
    path('movies/', movies_all, name='movies'),
    path('movies/review', movies_review, name='movies_review'),
    path('movies/thought', movies_thought, name='movies_thought'),
    path('movies/discuss', movies_discuss, name='movies_discuss'),
    # Anime pages
    path('animes/', animes_all, name='animes'),
    path('animes/review', animes_review, name='animes_review'),
    path('animes/thought', animes_thought, name='animes_thought'),
    path('animes/discuss', animes_discuss, name='animes_discuss'),
    # Manga pages
    path('mangas/', mangas_all, name='mangas'),
    path('mangas/review', mangas_review, name='mangas_review'),
    path('mangas/thought', mangas_thought, name='mangas_thought'),
    # Video game pages
    path('video-games/', video_games_all, name='video_games'),
    path('video-games/review', video_games_review, name='video_games_review'),
    path('video-games/thought', video_games_thought, name='video_games_thought'),
    # Musics pages
    path('musics/', musics_all, name='musics'),
    path('musics/thought', musics_thought, name='musics_thought'),
    path('musics/album', musics_album, name='musics_album'),
    path('musics/song', musics_song, name='musics_song'),

    # Post details
    path('posts/<int:pk>', post_view, name='post_view'),

    # About me page
    path('about-me/', about_me, name='about-me')
]
