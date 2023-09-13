from mysqlconnection import connectToMySQL
class User:
    def __init__(self,data):
        self.id= data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users # this is stating hey give me the list of users.

    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('users_schema').query_db( query, data)
        return cls(results[0])
    
#cls returns a list of dictionaries so we have to access it accordingly
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(f_name)s, last_name = %(l_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s"
        return connectToMySQL('users_schema').query_db( query, data)

    @classmethod
    def save(cls, data): # we have to pass in the data so we can access it and we almost must pass cls, like our instance of self, we mustb drag it along.
        query = "INSERT INTO users ( first_name, last_name, email, created_at) VALUES ( %(fname)s, %(lname)s, %(email)s, NOW() );"
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db( query, data )
    
