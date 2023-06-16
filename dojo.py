from mysqlconnection import connectToMySQL

class Dojo:
    db = "dojos_and_ninjas"

#needs to match database
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#get all method to display dojos 
    @classmethod
    def get_all_dojos(cls):
        query = """
            SELECT * FROM dojos;
        """
        #establishing connecting to db 
        results = connectToMySQL(cls.db).query_db(query)

        all_dojos = []
        
        for dojo in results:
            all_dojos.append(cls(dojo))
        return all_dojos
    
        #create a class method to save user in DB 
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"

        # comes back as the new row id
        result = connectToMySQL(cls.db).query_db(query,data)
        return result
    

#get one method 
    @classmethod
    def get_one(cls, dojo_id):
        query = 'SELECT * FROM dojos WHERE id = %(id)s'

        data = {
            'id': dojo_id
        }

        result = connectToMySQL(cls.db).query_db(query, data)
        return result[0]