from mysql.connector import connect

class database:
    def __init__(self):
        try:
            self.db = connect(host='localhost',
                            database='primadmi',
                            user='root',
                            password='Jakarta221')
        except Exception as e:
            print(e)
    
    def showUsers(self):
        cursor = self.db.cursor()
        query ='''select * from anggotas'''
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def showUserById(self, **params):
        cursor = self.db.cursor()
        query = '''
            select * 
            from anggotas 
            where userid = {0};
        '''.format(params["userid"])
        
        cursor.execute(query)
        result = cursor.fetchone()
        return result
            
    def showUserByEmail(self, **params):
        cursor = self.db.cursor()
        query = '''
            select * 
            from anggotas 
            where email = "{0}" ;
        '''.format(params["email"])
        
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    
    def insertUser(self, **params):
        column = ', '.join(list(params['values'].keys()))
        values = tuple(list(params['values'].values()))
        crud_query = '''insert into anggotas ({0}) values {1};'''.format(column, values)
        # print(crud_query)
        cursor = self.db.cursor()
        cursor.execute(crud_query)
    
    def updateUserById(self, **params):
        userid = params['userid']
        values = self.restructureParams(**params['values'])
        crud_query = '''update anggotas set {0} where userid = {1};'''.format(values, userid)

        cursor = self.db.cursor()
        cursor.execute(crud_query)
    
    def deleteUserById(self, **params):
        userid = params['userid']
        crud_query = '''delete from anggotas where userid = {0};'''.format(userid)

        cursor = self.db.cursor()
        cursor.execute(crud_query)

    def dataCommit(self):
        self.db.commit()
        
    def restructureParams(self, **data):
        list_data = ['{0} = "{1}"'.format(item[0],item[1]) for item in data.items()]
        result = ', '.join(list_data)
        return result