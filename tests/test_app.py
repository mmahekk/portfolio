import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        assert "<img src=\"../static/img/" in html
        assert "home"
        assert "about section" in html
        assert "experience section" in html
        assert "education section" in html
        assert "map section" in html
        
    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        
        # Test POST request to /api/timeline_post
        response = self.client.post("/api/timeline_post", 
                  data = {"name": "John Smith",
                          "email": "jsmith@example.com",
                          "content": "Hello world, I'm John Smith."})
        assert response.status_code == 200
        assert response.is_json
        assert "timeline_posts" in json
        json = response.get_json()
        assert json["id"] == 1
        assert json["name"] == "John Smith"
        assert json["email"] == "jsmith@example.com"
        assert json["content"] == "Hello world, I'm John Smith."
        
        # Test GET request to /api/timeline_post after making a POST request
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        assert json["timeline_posts"][0]["id"] == 1
        assert json["timeline_posts"][0]["name"] == "John Smith"
        assert json["timeline_posts"][0]["email"] == "jsmith@example.com"
        assert json["timeline_posts"][0]["content"] == "Hello world, I'm John Smith."
        
    def test_timeline_page(self):
        response = self.client.get('/timeline')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<title>Timeline</title>' in html
        assert '<h2>Timeline</h2>' in html
        assert '<label for="name">Name</label>' in html
        assert '<label for="email">Email</label>' in html
        assert '<label for="content">Content</label>' in html
        assert '<button id="addTimelinePost"' in html
        assert '<h2>Records</h2>' in html
        
    def test_malformed_timeline_post(self):
        # POST request with missing name
        response = self.client.post("/api/timeline_post", 
                                    data={"email": "john@example.com",
                                          "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html
        
        # POST request with empty content
        response = self.client.post("/api/timeline_post", 
                                    data={"name": "John Doe", 
                                          "email": "john@example.com",
                                          "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html
        
        # POST request with malformed email
        response = self.client.post("/api/timeline_post", 
                                    data={"name": "John Doe", 
                                          "email": "not-an-email",
                                          "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
