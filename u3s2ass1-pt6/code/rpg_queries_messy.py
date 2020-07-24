import os
import sqlite3

'''
Part 1: 

1. How many total Characters are there?
2. How many of each specific subclass?
3. How many total Items?
4. How many of the Items are weapons? How many are not?
5. How many Items does each character have? (Return first 20 rows)
6. How many Weapons does each character have? (Return first 20 rows)
7. On average, how many Items does each Character have?
8. On average, how many Weapons does each character have?

the charactercreator_* and armory_* tables and where you should focus your attention.

armory_item and charactercreator_character are the main tables for Items and Characters respectively -

It's also OK to figure out the results partially with a query and partially with a bit of logic or math afterwards, 
though doing things purely with SQL is a good goal. Subqueries and aggregation functions may be helpful for putting 
together more complicated queries.
'''

#from pprint import pprint  #from https://github.com/s2t2/lambda-ds-3-2/blob/master/app/chinook_queries.py

#construct a path to wherever your database exiSts; string path =? ABSOLUTE  FILE PATH CONSTRUCTION?
#DB_FILEPATH  = "chinook.db" a (hard-coded?) STRING for a path; (file..) works diff'ntly from how wld in app directory ... OTHER NON-reliable ways: 1) hardcoded with slashes 2) a STRING won't work depending on where yr trying to run it

#RELATIVE FILE PATH CONSTRUCTION
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3") # dirname(__file__) = metadata about the file

#RELIABLE CONNECTION PATH (to join filepaths.. https://www.youtube.com/watch?v=u8KHXaRUxjg&feature=youtu.be 1:51:11 in Mod1 vid)
connection = sqlite3.connect(DB_FILEPATH)
print("\n", "CONNECTION:",connection, '\n')

cursor = connection.cursor()
print(" CURSOR", cursor, "\n")   


#1. How many total Characters are there?
query1 = """SELECT count(distinct character_id) FROM charactercreator_character;"""
#query1 = "SELECT count(character_id) FROM charactercreator_character_inventory;"
#

#result = cursor.execture(query)
#print("RESULT", RESULT) # returns cursor object w/o results (need to fetch the results)

#breakpoint()

result1 = cursor.execute(query1).fetchall()
print("RESULT 1. Total Characters: ", result1)
print("------------------")
'''
2. How many of each specific (character) subclass? (mage-->necromancer, thief, cleric, fighter, )
    a) want a row per each subclass (ea subcls on its own row)
    b) want Result set to have 2 columns: 
       (i) 1 with subclass name; GROUP BY subclass name
       (ii) 1 with counts
    AGGREGATE/"drop" OTHER COLS WE'RE NOT GROUPING BY- we're Grouping by subclass?


query2 = "
SELECT 
	character_ptr_id,
	count(distinct character_ptr_id) 
	
FROM charactercreator_cleric,
     charactercreator_mage, 
     charactercreator_thief, 
     charactercreator_fighter,
     charactercreator_necromancer


GROUP BY character_ptr_id"  
    # in TablePlus gett err: Query 1 ERROR: ambiguous column name: character_ptr_id;
    # “Ambiguous column name” means that you are referencing an attribute or attributes that belong to more 
    # than one of the tables you are using in the query, and have not qualified the attribute reference. The SQL 
    # engine doesn't know which one you want. What does the SQL 'ambiguous column name' error mean ...

#OR?: 
#-----------------------
SELECT 

FROM charactercreator_cleric.character_ptr_id  # then do for all other subclasses 

#------------------ 

# MORE CONCISE/FANCY with MUTLIPLE TABLES JOINS, iterating through the queries:

queries = [
    #"SELECT COUNT(customerId) FROM customers;"
    "SELECT * FROM all_character_subcls"  # TO DO: make a TABLE &? a list of subclasses; or list ALL TABLES proLLY eaySia
                                          #   OR!: JOIN TABLES or/and COLS
]

for query in queries:
    print("--------------------")
    print(f"QUERY: '{query}'")

    #obj = curs.execute(query)
    #print("OBJ", type(obj))
    #print(obj) #> <class 'sqlite3.Cursor'>

    results = curs.execute(query).fetchall()
    print("RESULTS:", type(results))
    print(results)

    print(type(results[0])) #> type(results[0])
    #breakpoint()
     
    '''
#2. How many of each specific (character) subclass?
query2a = "SELECT count(distinct character_ptr_id) as total_clerics FROM charactercreator_cleric;"
result2a = cursor.execute(query2a).fetchall()
print("RESULT 2a. Total clerics: ", result2a)
print("--------------------")

query2b = "SELECT count(distinct character_ptr_id) as total_mages FROM charactercreator_mage;"
result2b = cursor.execute(query2b).fetchall()
print("RESULT 2b. Total mages: ", result2b)
print("--------------------")

query2c = "SELECT count(distinct character_ptr_id) as total_thieves FROM charactercreator_thief;"
result2c = cursor.execute(query2c).fetchall()
print("RESULT 2c. Total thieves: ", result2c)
print("--------------------")

'''  COMMENTING OUT BECAUSE ASSUMING necromancer subclass counts included in its Parent Class mage's counts
query2e = "SELECT count(distinct character_ptr_id) as total_necromancers FROM charactercreator_necromancer;"
result2e = cursor.execute(query2d).fetchall()
print("RESULT 2e. Total necromancers: ", result2e)
print("--------------------")
'''

query2d = "SELECT count(distinct character_ptr_id) as total_fighters FROM charactercreator_fighter;"
result2d = cursor.execute(query2d).fetchall()
print("RESULT 2d. Total fighters: ", result2d)
print("--------------------")


# -------- Question 2 using Row Factory connection object -------------

connection.row_factory = sqlite3.Row
print(type(connection), '\n') # <class 'sqlite3.Connection'> object(?)

cursor = connection.cursor()
print(type(cursor)) # <class 'sqlite3.Cursor'>

all_char_queries = """
    SELECT  # can try a tuple or dict? to correl8 respective subclasses
            # to their character_creator TABLE/Entity to use a "chained" SELECT CLAUSE?
        
        count(distinct character_ptr_id) as total_clerics
        
            FROM    charactercreator_cleric

            SELECT  count(distinct f.character_ptr_id) as total_fighters
            FROM    charactercreator_fighter

            SELECT  count(distinct m.character_ptr_id) as total_mages
            FROM    charactercreator_mage

            SELECT  count(distinct n.mage_ptr_id) as total_necromancers
            FROM    charactercreator_necromancer      
                
            SELECT  count(distinct t.character_ptr_id) as total_thieves
            FROM    charactercreator_thief

                 """      

'''
all_char_queries = """
    SELECT
        count(distinct c.character_ptr_id) as total_clerics,
        count(distinct f.character_ptr_id) as total_fighters,
        count(distinct m.character_ptr_id) as total_mages,
        count(distinct n.mage_ptr_id) as total_necromancers,
        count(distinct t.character_ptr_id) as total_thieves
    FROM charactercreator_character ccc

        LEFT JOIN charactercreator_fighter f
            ON ccc.character_id = f.character_ptr_id
        
        LEFT JOIN charactercreator_cleric c
            ON ccc.character_id = c.character_ptr_id

        LEFT JOIN charactercreator_mage m
            ON ccc.character_id = m.character_ptr_id

        LEFT JOIN charactercreator_necromancer n
            ON ccc.character_id = n.mage_ptr_id

        LEFT JOIN charactercreator_thief t
            ON ccc.character_id = t.character_ptr_id
                    """          
'''
   
#SELECT all the respective character types (total numbers of)
#FROM charactercreator_character table, aliasing it as "ccc"
#and LEFT JOIN charactercreator_character table with the
#"character_id" COLUMN that is a MATCH with or =  the "character_ptr_id" 
#COLUMN TABLES named (on the fly)- they are not defined elsewhere, those letters)
# "c, f, m, n, t

'''
result2 = cursor.execute(all_char_queries).fetchall()
print("Result 2. Totals from all subclasses: ", result2) 
#print(result2['all_char_queries'])
#print(result2)
'''


#print("---------------------------")


#3. How many total Items?
# Seems charactercreator_inventory itemizes an item_id a char has per line; indexed by line#(?)
#   a given character_id tends to have >1  item_ids associ8d with it (on >1 row)  

query3 = """
SELECT count(DISTINCT item_id) as total_items
  FROM armory_item
         """ 
result3 = cursor.execute(query3).fetchall()
print("Result 3. Total items: ", result3)


#-----------FALSE STARTS----------------
"""
    SELECT count(distinct item_id) 
      FROM charactercreator_inventory

NOT SUPPORTED in TABLEPLUS:
SELECT * 
  FROM charactercreator_character_inventory A
  FULL OUTER JOIN armory_weapon B
   
"""
#-----------------------------------    

# 4. How many of the Items are weapons? How many are not?

print("--------------------------------")

query4 = """
SELECT count(DISTINCT item_ptr_id) as total_weapons
 FROM armory_weapon
         """
result4 = cursor.execute(query4).fetchall()
print("Result 4. Total weapons: ", result4)         
print(result4["total_weapons"] )

print("--------------------------------")








