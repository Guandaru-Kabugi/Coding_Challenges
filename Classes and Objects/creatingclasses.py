class User:
   def __init__(self,user_id, username): #always remember to use the self
      self.id = user_id
      self.name = username
      self.followers = 0
      self.following = 0
   def follow (self,user): #remember to use the self.
       user.followers +=1
       self.following +=1
        



user_1 = User(5546,"Alex") #we use the parameters in the init function when creating the object
print(user_1.name)
user_2 = User(6762,"James") #we use the parameters in the init function when creating the object
print(user_1.name)
print(user_2.id)
print(user_1.followers)
user_1.follow(user_2)
print()
print(user_1.followers) #since user_1 is the one following, it has not yet gotten followed, so result is zero
print(user_1.following) #since user_1 is the one following, it has one following
print(user_2.followers) #since user_2 is the one being followed, it has one follower
print(user_2.following) #since user_2 is the one being followed, it has zero following because it is not following anyone
