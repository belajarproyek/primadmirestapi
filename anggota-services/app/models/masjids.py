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
    
    def showMasjidByEmail(self, **params):
        cursor = self.db.cursor()
        
        query ='''select anggotas.nama ,masjids.* 
        from masjids
        inner join anggotas on masjids.userid = anggotas.userid
        where anggotas.email = "{0}" and masjids.isactive = 1;
        '''.format(params["email"])
        
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
    def insertMasjid(self, **params):
        column = ', '.join(list(params.keys()))
        values = tuple(list(params.values()))
        crud_query = '''insert into masjids ({0}) values {1};'''.format(column, values)
        # print(crud_query)
        cursor = self.db.cursor()
        cursor.execute(crud_query)
    
    def updateMasjidStatus(self, **params):
        masjidid = params['masjidid']
        values = self.restructureParams(**params)
        crud_query = '''update masjids set isactive = 0 where masjidid = {1};'''.format(values,masjidid)

        cursor = self.db.cursor()
        cursor.execute(crud_query)

    def dataCommit(self):
        self.db.commit()
        
    def restructureParams(self, **data):
        list_data = ['{0} = "{1}"'.format(item[0],item[1]) for item in data.items()]
        result = ', '.join(list_data)
        return result
    
    
    
