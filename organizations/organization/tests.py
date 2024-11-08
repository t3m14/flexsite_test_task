from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Organization
from .serializers import OrganizationSerializer
from user.models import User

class OrganizationModelTest(APITestCase):
    def setUp(self):
        self.organization = Organization.objects.create(
            name='Test Organization',
            description='A description for test organization'
        )

    def test_organization_creation(self):
        self.assertIsInstance(self.organization, Organization)
        self.assertEqual(self.organization.name, 'Test Organization')
        self.assertEqual(self.organization.description, 'A description for test organization')

    def test_string_representation(self):
        self.assertEqual(str(self.organization), self.organization.name)


class OrganizationViewSetTest(APITestCase):
    def setUp(self):
        self.organization_data = {
            'name': 'Test Organization',
            'description': 'A description for test organization'
        }
        self.organization = Organization.objects.create(**self.organization_data)
        #auth
        self.user = User.objects.create_user(email='testuser@example.com', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.url = reverse('organization')  # Adjust if needed (e.g., 'organization-list' should match the name in your urls)
        self.create_url = reverse('create-organization')
    def test_create_organization(self):
        response = self.client.post(self.create_url, self.organization_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Organization.objects.count(), 2)  # One created in setUp and one now
        self.assertEqual(Organization.objects.get(id=response.data['id']).name, 'Test Organization')

    def test_list_organizations(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Adjust according to the count of organizations created

class CreateOrganizationViewTest(APITestCase):
    def setUp(self):
        # auth
        self.user = User.objects.create_user(email='testuser@example.com', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.url = reverse('create-organization')  

    def test_create_organization_invalid(self):
        invalid_data = {'name': '', 'description': 'No name organization'}
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)

    def test_create_organization_valid(self):
        valid_data = {
            'name': 'Valid Organization Name',
            'description': 'This is a valid organization description.'
        }
        response = self.client.post(self.url, valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Organization.objects.count(), 1)  # Ensure one org has been created
