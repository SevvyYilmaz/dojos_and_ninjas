from mysqlconnection import connectToMySQL


class Ninja:
    db = "dojos_and_ninjas"

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);"

        # comes back as the new row id
        result = connectToMySQL(cls.db).query_db(query,data)
        return result


    @classmethod
    def get_all_ninjas_from_dojo (cls, dojo_id):
        query = """
            SELECT * FROM ninjas 
            WHERE dojo_id = %(dojo_id)s;
        """
        data = {'dojo_id':dojo_id}
        #establishing connecting to db 
        results = connectToMySQL(cls.db).query_db(query,data)

        all_ninjas = []
        
        for ninja in results:
            all_ninjas.append(ninja)
        return all_ninjas
