import os

from django.test import TestCase

# Create your tests here.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'awwwards.settings')
import django
django.setup()

from .models import User, Project, Profile, Rating, AvgRating


# Create your tests here.
class RatingTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345")
        # self.test_category.save_category()

        self.test_project = Project(creator=self.test_user, name="The test project", tags="tag1 tag2",
                                    screenshot_1='galleria_imgs/hobbies_7.jpg',
                                    screenshot_2='galleria_imgs/hobbies_7.jpg',
                                    screenshot_3='galleria_imgs/hobbies_7.jpg',
                                    description="test_loc")

        self.test_rating = Rating(reviewer=self.test_user, project=self.test_project, design=6, usability=9, content=7)

    # testing instance
    def test_instance(self):
        rating = self.test_rating
        self.assertEqual(self.test_rating, rating)

    # testing save method
    def test_add_rating_method(self):
        original_len = Rating.get_all_ratings()
        print(f'original len {len(original_len)}')
        self.test_project.save_project()
        self.test_rating.add_rating()

        new_len = Rating.get_all_ratings()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_rating_method(self):
        self.test_project.save_project()
        self.test_rating.add_rating()
        original_len = Rating.objects.all()
        print(f'the categorys are{len(original_len)}')
        Rating.delete_rating(self.test_rating.id)
        new_len = Rating.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_rating_by_id_method(self):
        self.test_project.save_project()
        self.test_rating.add_rating()
        req_result = Rating.get_rating_by_id(self.test_rating.id)
        self.assertTrue(req_result is not None)

    def test_search_project_by_reviewer_id_method(self):
        self.test_project.save_project()
        self.test_rating.add_rating()

        req_result = Rating.search_rating_by_reviewer_id(self.test_rating.reviewer.id)
        self.assertTrue(req_result is not None)


# Create your tests here.
class AvgRatingTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345")
        # self.test_category.save_category()

        self.test_project = Project(creator=self.test_user, name="The test project", tags="tag1 tag2",
                                    screenshot_1='galleria_imgs/hobbies_7.jpg',
                                    screenshot_2='galleria_imgs/hobbies_7.jpg',
                                    screenshot_3='galleria_imgs/hobbies_7.jpg',
                                    description="test_loc")

        self.test_rating = AvgRating(project=self.test_project, design=6, usability=9, content=7)

    # testing instance
    def test_instance(self):
        rating = self.test_rating
        self.assertEqual(self.test_rating, rating)

    # testing save method
    def test_add_rating_method(self):
        original_len = AvgRating.get_all_avg_ratings()
        print(f'original len {len(original_len)}')
        self.test_project.save_project()
        self.test_rating.add_rating()

        new_len = AvgRating.get_all_avg_ratings()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_rating_method(self):
        self.test_project.save_project()
        self.test_rating.add_rating()
        original_len = AvgRating.objects.all()
        print(f'the categorys are{len(original_len)}')
        AvgRating.delete_avg_rating(self.test_rating.id)
        new_len = AvgRating.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_rating_by_id_method(self):
        self.test_project.save_project()
        self.test_rating.add_rating()
        req_result = AvgRating.get_avg_rating_by_id(self.test_rating.id)
        self.assertTrue(req_result is not None)

    def test_search_project_by_reviewer_id_method(self):
        self.test_project.save_project()
        self.test_rating.add_rating()

        req_result = AvgRating.search_avg_rating_by_project_id(self.test_project.id)
        self.assertTrue(req_result is not None)


class ProfileTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345")
        # self.test_category.save_category()

        # self.test_local_user = Like(user=self.test_user, user=self.test_user)

        self.test_profile = Profile(user=self.test_user, profile_img='galleria_imgs/hobbies_7.jpg',
                                    bio="test_loc", website="Thewe.com",)


    # testing instance
    def test_instance(self):
        profile = self.test_profile
        self.assertEqual(self.test_profile, profile)

    # testing save method
    def test_save_profile_method(self):
        original_len = Profile.get_all_profiles()
        print(f'original len {len(original_len)}')
        self.test_profile.save_profile()

        new_len = Profile.get_all_profiles()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_profile_method(self):
        self.test_profile.save_profile()
        original_len = Profile.objects.all()
        print(f'the categorys are{len(original_len)}')
        Profile.delete_profile(self.test_profile.id)
        new_len = Profile.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_profile_by_id_method(self):
        self.test_profile.save_profile()
        req_result = Profile.get_profile_by_id(self.test_profile.id)
        self.assertTrue(req_result is not None)

    def test_search_profile_by_website_method(self):
        self.test_profile.save_profile()

        req_result = Profile.search_profile_by_website(self.test_profile.website)
        self.assertTrue(req_result is not None)


class ProjectTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345")
        # self.test_category.save_category()

        # self.test_local_user = Like(user=self.test_user, user=self.test_user)

        self.test_project = Project(creator=self.test_user, name="The test project", tags="tag1 tag2",
                                    screenshot_1='galleria_imgs/hobbies_7.jpg',
                                    screenshot_2='galleria_imgs/hobbies_7.jpg',
                                    screenshot_3='galleria_imgs/hobbies_7.jpg',
                                    description="test_loc")

    # testing instance
    def test_instance(self):
        project = self.test_project
        self.assertEqual(self.test_project, project)

    # testing save method
    def test_save_profile_method(self):
        original_len = Project.get_all_projects()
        print(f'original len {len(original_len)}')
        self.test_project.save_project()

        new_len = Project.get_all_projects()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_profile_method(self):
        self.test_project.save_project()
        original_len = Project.objects.all()
        print(f'the categorys are{len(original_len)}')
        Project.delete_projects(self.test_project.id)
        new_len = Project.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_profile_by_id_method(self):
        self.test_project.save_project()
        req_result = Project.get_project_by_id(self.test_project.id)
        self.assertTrue(req_result is not None)

    def test_search_project_by_name_method(self):
        self.test_project.save_project()

        req_result = Project.search_project_by_name(self.test_project.name)
        self.assertTrue(req_result is not None)


