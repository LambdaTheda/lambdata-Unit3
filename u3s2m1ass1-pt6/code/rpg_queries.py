import sqlite3
import os

#DB_FILEPATH = "data/chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")
conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row
print(type(conn)) #> <class 'sqlite3.Connection'>
curs = conn.cursor()
print(type(curs)) #> <class 'sqlite3.Cursor'>


query = """SELECT 
count(DISTINCT character_id) as character_count
FROM charactercreator_character"""

# query1 = """SELECT 
# count(DISTINCT character_ptr_id) as character_ptr_count
# FROM charactercreator_cleric"""

# query2 = """SELECT 
# count(DISTINCT character_ptr_id) as character_ptr_count
# FROM charactercreator_fighter"""

# query3 = """SELECT 
# count(DISTINCT character_ptr_id) as character_ptr_count
# FROM charactercreator_mage"""

# query4 = """SELECT 
# count(DISTINCT character_ptr_id) as character_ptr_count
# FROM charactercreator_thief"""

queries_combined = """SELECT 
    
        count(distinct c.character_ptr_id) as total_clerics
        ,count(distinct f.character_ptr_id) as total_fighters
        ,count(distinct m.character_ptr_id) as total_mages
        ,count(distinct n.mage_ptr_id) as total_necromancers
        ,count(distinct t.character_ptr_id) as total_thieves
FROM charactercreator_character ccc 
LEFT JOIN charactercreator_fighter f  
    ON ccc.character_id = f.character_ptr_id
LEFT JOIN charactercreator_cleric c 
    ON ccc.character_id= c.character_ptr_id
LEFT JOIN charactercreator_mage m 
    ON ccc.character_id =  m.character_ptr_id
LEFT JOIN charactercreator_necromancer n 
    ON ccc.character_id = n.mage_ptr_id
LEFT JOIN charactercreator_thief t 
    ON ccc.character_id = t.character_ptr_id"""

query5 = """SELECT 
count(DISTINCT item_id ) as total_item
FROM armory_item"""

query6 = """SELECT 
count(DISTINCT item_ptr_id) as weapons
FROM armory_weapon"""

query7 = """SELECT 
count(DISTINCT item_id)  -  count(DISTINCT item_ptr_id) as total_non_weapons
FROM armory_item, armory_weapon"""

query8 = """SELECT item_id
, count(DISTINCT item_id) as item 
FROM charactercreator_character_inventory
GROUP BY character_id 
LIMIT 20 
"""
query9 = """SELECT cci.character_id
, count(DISTINCT aw.item_ptr_id) as number_of_weapons
FROM charactercreator_character_inventory as cci
LEFT JOIN armory_item as ai ON cci.item_id = ai.item_id
LEFT JOIN armory_weapon as aw ON ai.item_id = aw.item_ptr_id
GROUP BY character_id
LIMIT 20"""

query10 = """SELECT avg(total_items) as avg_items
FROM (
    -- row per character = 302
    SELECT 
        c.character_id
        ,c.name
        --,ci.item_id
        ,count(distinct ci.item_id) as total_items
        
    FROM charactercreator_character c 
    LEFT JOIN charactercreator_character_inventory ci 
        ON c.character_id = ci.character_id
    GROUP BY c.character_id
) subz"""

query11 = """SELECT avg(weapon_count) as avg_weapon
FROM (
	SELECT
	 cci.character_id
	 ,count(DISTINCT aw.item_ptr_id) as weapon_count
	 
	FROM charactercreator_character_inventory cci
	LEFT JOIN armory_item ai ON cci.item_id = ai.item_id
	LEFT JOIN armory_weapon aw ON ai.item_id = aw.item_ptr_id
	GROUP BY 1
) subz"""


print("----------")
result = curs.execute(query).fetchone()
print("RESULTS FOR CHARACTERCREATOR_CHARACTER", result)
print(result["character_count"])
# print("-------------")
# result1 = curs.execute(query1).fetchone()
# print("Results for charactercreator_cleric", result1)
# print(result1["character_ptr_count"])
# print("---------")
# result2 = curs.execute(query2).fetchone()
# print("Results for charactercreator_fighter", result2)
# print(result2["character_ptr_count"])
# print("---------")
# result3 = curs.execute(query3).fetchone()
# print("Results for charactercreator_mage", result3)
# print(result3["character_ptr_count"])
# print('--------')
# result4 = curs.execute(query4).fetchone()
# print("Results for charactercreator_thief", result4)
# print(result4["character_ptr_count"])
# print("-------------")
# result5 = curs.execute(query5).fetchone()
# print("Results for total Items", result5)
# print(result5["total_item"])

result_queries = curs.execute(queries_combined).fetchall()
print("Results of each specific subclass", result_queries)


result6 = curs.execute(query6).fetchone()
print("Results for total weapons", result6)
print(result6["weapons"])
print("---------")

result7 = curs.execute(query7).fetchone()
print("Results for total non weapons", result7)
print(result7["total_non_weapons"])
print("---------")

result8 = curs.execute(query8).fetchall()
for rw in result8:
    print(rw[0], rw[1])
print("---------")

result9 = curs.execute(query9).fetchall()
for rw in result9:
    print(rw['character_id'], rw['number_of_weapons'])
print("---------")

result10 = curs.execute(query10).fetchone()
print("Average item per character", result10)
print(result10["avg_items"])
print("---------")

result11= curs.execute(query11).fetchone()
print("Average weapon per character", result11)
print(result11["avg_weapon"])
print("---------")