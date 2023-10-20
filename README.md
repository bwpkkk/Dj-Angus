# Dj-Angus
Update on 2023-10-20:
1. Changed some fields into many-to-many fields in Student model because many students can have many courses and many teachers.
2. Added the tags in the end of each model so the query set returns the name of each object instead of Object1,Object2...
  
        def __str__(self):
       return self.username

3. Added a navbar to the index page, in order to browse the courses.
      
