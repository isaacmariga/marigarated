from django.test import TestCase
from .models import Profile, Review, Projects

# Create your tests here.
class ProjectsTest(TestCase):
    '''
    test class for Projects model
    '''
    def setUp(self):
        '''
        test method to create Image instances called before all tests
        '''
        self.new_category = Review(name='testing')
        self.new_category.save_category()
        
        self.new_location = Profile(city='Nairobi', country='Kenya')
        self.new_location.save_location()
        
        self.new_picture = Projects(image_link='Projects/picture.jpeg', title='Image title', description='sth random', category=self.new_category, location=self.new_location)
        self.new_picture.save_image()
        self.another_picture = Projects(image_link='Projects/photo.jpg', title='Another title', description='sth else more random', category=self.new_category, location=self.new_location)
        self.another_picture.save_image()

    def tearDown(self):
        '''
        test method to delete Image instances after each test is run
        '''
        Review.objects.all().delete()
        Profile.objects.all().delete()
        Projects.objects.all().delete()

    def test_instances(self):
        '''
        test method to assert instances created during setUp
        '''
        self.assertTrue(isinstance(self.new_picture,Projects))
        self.assertTrue(isinstance(self.new_category, Review))
        self.assertTrue(isinstance(self.new_location, Profile))

    def test_save_image(self):
        '''
        test method to ensure an Image instance has been correctly saved
        '''
        self.assertTrue(len(Projects.objects.all()) == 2)

    def test_delete_image(self):
        '''
        test method to ensure an Image instance has been correctly deleted
        '''
        self.new_picture.delete_image()
        self.assertTrue(len(Projects.objects.all()) == 1)

    def test_update_image(self):
        '''
        test method to ensure an Image instance has been correctly updated
        '''
        update_test = self.new_picture.update_image('Projects/updated.png')
        self.assertEqual(update_test.image_link, 'Projects/updated.png')

    def test_get_all(self):
        '''
        test method to ensure all instances of Image class have been retrieved
        '''
        pictures = Projects.get_all()
        # print(pictures)

    def test_get_image_by_id(self):
        '''
        test method to ensure Image instances can be retrieved by id
        '''
        obtained_image = Projects.get_image_by_id(self.another_picture.id)
        # print(obtained_image.title)

    def test_search_image(self):
        '''
        test method to ensure correct searching of an multiple image instances by category
        '''
        obtained_image = Projects.search_image(self.new_picture.category)
        # print(obtained_image)

    def test_filter_by_location(self):
        '''
        test method to obtain image insatnces by location
        '''
        obtained_image = Projects.filter_by_location(self.another_picture.location)
        print(obtained_image)



class CategoryTest(TestCase):
    '''
    test class for Review model
    '''
    def setUp(self):
        '''
        test method to create Category instances called before all tests
        '''
        self.new_category = Review(name='categoryA')
        self.new_category.save_category()

    def tearDown(self):
        '''
        test method to delete Category instances after each test is run
        '''
        Review.objects.all().delete()

    def test_save_category(self):
        '''
        test method to ensure a Category instance has been correctly saved
        '''
        self.assertTrue(len(Review.objects.all()) == 1)     

    def test_delete_category(self):
        '''
        test method to ensure a Category instance has been correctly deleted
        '''
        self.new_category.save_category()
        self.new_category.delete_category()
        self.assertTrue(len(Review.objects.all()) == 0)    

    def test_update_category(self):
        '''
        test method to ensure a Category instance has been correctly updated
        '''
        update_cat = Review.update_category('categoryA', 'differentCat')
        self.assertEqual(update_cat.name, 'differentCat')




class LocationTest(TestCase):
    '''
    test class for Profile model
    '''
    def setUp(self):
        '''
        test method to create Location instances called before all tests
        '''
        self.new_location = Profile(city='lost city', country='unknown')
        self.new_location.save_location()

    def test_save_location(self):
        '''
        test method to ensure a Location instance has been correctly saved
        '''
        self.assertTrue(len(Profile.objects.all()) == 1)     

    def test_delete_location(self):
        '''
        test method to ensure a Location instance has been correctly deleted
        '''
        self.new_location.save_location()
        self.new_location.delete_location()
        self.assertTrue(len(Profile.objects.all()) == 0)

    def test_update_location(self):
        '''
        test method to ensure a Location instance has been correctly updated
        '''
        update_locale = Profile.update_location('unknown', 'paperTown')
        self.assertEqual(update_locale.city, 'paperTown')

    def test_get_all(self):
        '''
        test method to ensure all instances of Profile class have been retrieved
        '''
        Profile = Profile.get_all()
        print(Profile)