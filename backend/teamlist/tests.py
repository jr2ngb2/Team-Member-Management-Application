from django.test import TestCase
from django.urls import reverse

from .models import TeamMember

class TeamMemberTests(TestCase):

    def setUp(self):
        TeamMember.objects.create(first_name="Neelendu" , last_name="Wadhwa" , email="test@gmail.com" , phone="9982145782")


    def test_TeamMember_name(self):
        member = TeamMember.objects.get(id=1)
        expected_first_name = f'{member.first_name}'
        self.assertEquals(expected_first_name , 'Neelendu')

    def test_TeamMember_list_view(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code , 200)
        self.assertContains(response , 'Neelendu')
        self.assertTemplateUsed(response , 'listusers.html')    


    def test_create_member(self):
        data = {
            "first_name":"Neelendu",
            "last_name" : "Wadhwa",
            "email":"test@gmail.com",
            "phone":"9982145782"
        }

        response = self.client.get(reverse('create'))
        self.assertTemplateUsed(response , "createuser.html")
        self.assertContains(response , "first_name")
        self.assertContains(response , "last_name")
        response = self.client.post("/create" , data=data)
        self.assertEqual(TeamMember.objects.count() , 1)
        

