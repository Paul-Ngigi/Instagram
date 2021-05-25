from django.test import TestCase
from .models import Post, Comment, Like, Follow
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your tests here.
class TestPostClass(TestCase):
    """
    Test class that test posts objects
    """

    # Setup method
    def setUp(self) -> None:
        self.new_user = User(full_name='Paul Ngigi', email='paul@gmail.com')
        self.new_user.save()

        self.new_post = Post(user=self.new_user, image='default.png', caption='cool pic')

    # Teardown method
    def tearDown(self) -> None:
        self.new_post.save()
        self.new_post.delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    # Testing saving post
    def test_save_post(self):
        self.new_post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    # Testing deleting post
    def test_delete_post(self):
        self.new_post.save_post()
        posts = Post.objects.all()

        self.new_post.delete_post()

        self.assertTrue(len(posts) < 1)


class TestCommentClass(TestCase):
    """
    Test class to test comment class properties
    """

    # Setup method
    def setUp(self) -> None:
        self.new_user = User(full_name='Paul Ngigi', email='paul@gmail.com')
        self.new_user.save()

        self.new_post = Post(user=self.new_user, image='default.png', caption='cool pic')
        self.new_post.save()

        self.new_comment = Comment(post=self.new_post, user=self.new_user, text='I like it')

    # Teardown method
    def tearDown(self) -> None:
        self.new_comment.save()
        self.new_comment.delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(self.new_comment, Comment)

    # Testing saving comment
    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comment.objects.all()

        self.assertTrue(len(comments) > 0)

    # Testing deleting comment
    def test_delete_comment(self):
        self.new_comment.save_comment()
        comments = Comment.objects.all()

        self.new_comment.delete_comment()
        self.assertTrue(len(comments) < 1)
