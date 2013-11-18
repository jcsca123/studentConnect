#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

DEFAULT_COURSE_NAME = 'default-course'

import webapp2
from google.appengine.ext import ndb

def course_key(class_name=DEFAULT_COURSE_NAME):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Courses', class_name)

class Message(ndb.Model):
    msg = ndb.TextProperty()
    user = ndb.TextProperty()
    time = ndb.TimeProperty(auto_now_add=True)
    slug = ndb.StringProperty()

 
class Courses(ndb.Model):
	slug = ndb.TextProperty()
	course = ndb.TextProperty()
	crn = ndb.TextProperty()
	prof = ndb.TextProperty()

class MessageHandler(webapp2.RequestHandler):
    def get(self, message):
        #self.response.write('message ' + message)
        #test = Message()
        #test.msg = 'Hello'
        #test.user = 'Bob'
        #test.slug = message
        #test.put()

        messageQuery = Message.query()
        messageQuery = messageQuery.filter(Message.slug == message)
        messageQuery.order(-Message.time)
        messages = messageQuery.fetch(100)
        output = '['
        for message in messages:
            output += '{"user":"' + message.user + '",'
            output += '"message":"' + message.msg + '",'
            output += '"time":"' + str(message.time) + '",'
            output += '"slug":"' + message.slug + '"},'

        output += '{"user":"fake message", "message": "fake message", "time": "fake message"}]'

        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        self.response.write(output)

    def post(self, message):
        #self.response.write('slug ' + message)
        #self.response.write('\nuser ' + self.request.get('user'))
        #self.response.write('\nmessage ' + self.request.get('message'))
        newMsg = Message()
        newMsg.msg = self.request.get('message')
        newMsg.user = self.request.get('user')
        newMsg.slug = message
        newMsg.put()

class CourseHandler(webapp2.RequestHandler):
    def get(self):
    	test = Courses(parent=course_key('Hello'))
    	test.slug = "linear-algebra"
    	test.course = "Linear Algebra"
    	test.crn = "12314"
    	test.prof = "daklfaskldfj"
    	test.put()
    	course_query = Courses.query(ancestor=course_key('Hello'))
    	courses = course_query.fetch(10)
    	output = '['
    	for course in courses:
    		output += "{\"slug\":\"" + course.slug + "\","
    		output += "\"course\":\"" + course.course + "\","
    		output += "\"id\":\"" + course.crn + "\","
    		output += "\"prof\":\"" + course.prof + "\"},"

    	output += "{\"slug\":\"fake-class\",\"course\":\"fake class\",\"id\":\"12353\",\"prof\":\"33456456\"}]"

        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        

    	self.response.write(output)

        

app = webapp2.WSGIApplication([
    webapp2.Route('/class', handler = CourseHandler, name = 'home'),
    webapp2.Route('/class/<message>', handler = MessageHandler, name = 'message')
], debug=True)
