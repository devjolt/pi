from .p15_logic import *
from random import randint


questions = {

    'DBMS': {
        'question':"Considering a 'DBSM', which of the following is PLACEHOLDER?",
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'1.1.1',
        'correct':(
            ('D stands for database'),
            ('M stands for management'),
            ('S stands for system'),
            ("the DBSM is software"),
            ("it is responsile for creating a database structure"),
            ('it is used to insert data'),
            ("it is used to update data"),
            ("it is used to delete data"),
            ("it is used to search data"),
            ('it ensures data security'), 
            ('it is responsible for transaction management'), 
            ('it ensures concurrent access to data for many users'),
            ('it enables data exchange with other database systems'),
        ),
        'incorrect': (
            ('D stands for datamining'),
            ('D stands for data-secure'),
            ('B stands for binary'),
            ('M stands for m'),
            ('S stands for sychnronised'),
            ("the DBSM is hardware"),
            ('it is used to upload data'),
            ("it is used to download data"),
            ("it is a complete data presentation package"),
            ("it is a data mining programme"),
            ('it does not have security features by default'), 
            ('it is not responsible for transaction management'), 
            ('it ensures access to data for one user at a time'),
            ('it is usually incompatible with other DBMS systems'),
        )
    },
    'Structured Query Language': {
        'question':"Which of the following is PLACEHOLDER?",
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'1.1.1',
        'correct':(
            'SQL stands for structured query language',
            'SQL is used to manage data in relational database management systems',
            'SQL is a domain specific programming language',
            'SQL is not a general purpose programming language'
            'RDBMS stands for relational database management system',
            'SQL arguably consists of a data query language (DQL), a data definition language (DDL), a data control language (DCL) and a data manipulation language (DML)',
            'SQL is a declarative language with proceedural elements',
            'SQL includes a data query language (DQL)',
            'SQL includes a data definition language (DDL)',
            'SQL includes a data control language (DCL)',
            'SQL includes a data manipulation language (DML)',
        ),
        'incorrect': (
            'SQL stands for standard query language',
            'SQL stands for structured query literal',
            'SQL stands for structured question language',
            'SQL is a general purpose programming language', 
            'SQL is an functional language',
            'SQL is an object oriented language',
            'SQL does not include a data query language',
            'SQL does not include a data definition language (DDL)',
            'SQL does not include a data control language (DCL)',
            'SQL does not include a data manipulation language (DML)',
        )
    },
    'Database entities': {
        'question':"Which of the following is PLACEHOLDER?",
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'1.1.1',
        'correct':(
            'a database can contain one or many tables',
            'a table can contain one or more records or rows',
            'a table can contain one or more fields or columns',
            'a record is a horizontal entity',
            'a field is a vertical entitiy',
            'each field in a table is represented by a column',
            'each record in a table is represented by a row', 
            'each field in a table has a name',
            'each table in a database has a name',
            'a record is a group of related fields',
            'fields contain defined types of data '
        ),
        'incorrect': (
            'a table can contain one or more databases',
            'a row can contain one or more tables',
            'a field can contain one or more tables',
            'a field can contain one or more records',
            'a record is a vertical entity',
            'a field is a horizontal entitiy',
            'each field in a table is represented by a row',
            'each record in a table is represented by a column', 
            'each record in a table has a name',
            'tables in a database are never named',
            'a field is a group of related tables',
            'field data type is never specified'
        )
    },
    'Popular databases': {
        'question':"Which of the following is PLACEHOLDER a relational database which uses SQL:",
        'positive':'',
        'negative':'not',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'course_code':'1.1.2',
        'correct':(
            'MySQL',
            'Microsoft / Sybase',
            'MonetDB',
            'Oracle',
            'PostgreSQL',
            'SAP HANA',
            'MongoDB',
            'IBM DB2',
            'Sqlite'
            ),
        'incorrect': (
            'PythonDB',
            'JavaDB',
            'JavaScriptDB',
            'CythonDB',
            'PythonDB',
            'GoDB',
            'FortranDB',
            'Monacle', 
            'TorSQL'
            )
        },
    'About sqlite': {
        'question':"Which of the following is PLACEHOLDER:",
        'positive':'correct',
        'negative':'incorrect',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'course_code':'1.1.3',
        'correct':(
            'SQlite3 module has been available in Python since version 2.5',
            'SQlite3 module provides a DB-API 2.0 interface',
            'DB-API 2.0 specification is described by PEP 249',
            'SQLite is a C library',
            'SQLite writes data directly to a file',
            'SQLite does not require a server to communicate with the DB',
            'SQLite doesn\'t require any configuration',
            'SQLite supports transactions',
            'SQLite can be used in mobile applications',
            'SQLite files are cross platform',
            'SQLite database files can be copied between 32 adn 64 bit systems'
            ),
        'incorrect': (
            'SQLite is a Python library',
            'SQLite is c# library',
            'SQLite is a c++ library',
            'SQLite writes data directly to a database',
            'SQLite requires a server to communicate with the DB',
            'SQLite requires careful configuration',
            'SQLite transactions are real time',
            'SQLite is only used on desktop',
            'SQLite can not be used in mobile applications',
            'SQLite files are platform specific',
            '32 bit SQLite files are incompatible with 64 bit systems',
            '64 bit SQLite files are incompatible with 32 bit systems',
            f'SQlite{randint(1,2)} module has been available in Python since version {randint(1,3)}.{randint(1,9)}',
            f'SQlite3 module provides a Postgres API interface',
            f'DB-API 2.0 specification is described by PEP {randint(100, 248)}',
            f'DB-API 2.0 specification is described by PEP {randint(250, 300)}',
            )
        },

    'Sqlite with Python': {
        'question':"Which of the following could PLACEHOLDER be valid code:",
        'positive':'',
        'negative':'not',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'course_code':'1.1.4',
        'correct':(
            '$import sqlite3',
            '$import sqlite3 as s',
            '$import sqlite3 as sql',
            "$conn = sqlite3.connect('hello.db')",
            "$conn = sqlite3.connect('C:\sqlite\hello.db')",
            "$conn = sqlite3.connect(':memory:')",
            "$c = sqlite3.connect('hello.db')",
            "$c = sqlite3.connect('C:\sqlite\hello.db')",
            "$c = sqlite3.connect(':memory:')",
            "$c = conn.cursor()",
            "$conn.commit()",
            "$conn.close()",
            ),
        'incorrect': (
            '$import sqlite',
            '$from sqlite3 import sqlite3',
            '$from sqlite3 import s',
            '$import sqlite3 import sql',
            "$conn = sqlite3.conn('hello.db')",
            "$conn = sqlite3.conn('C:\sqlite\hello.db')",
            "$conn = sqlite3.conn(':memory:')",
            "$conn = sqlite3.connect(hello.db)",
            "$conn = sqlite3.connect(C:\sqlite\hello.db)",
            "$conn = sqlite3.connect(:memory:)",
            "$conn = sqlite3.connect('hello')",
            "$conn = sqlite3.connect('C:\sqlite\hello')",
            "$conn = sqlite3.connect('memory')",
            "$conn = sqlite3.connect('::memory::')",
            "$c = conn.curse()",
            "$c = cursor.conn()",
            "$conn.save()",
            "$conn.end()",
            "$conn.transfer()",
            "$conn.disconnect()",
            )
        },

    'Python sqlite': {
        'question_with_0':['Which comment would best fit the following code?','PLACEHOLDER'],
        'question_with_1':'Which snippet will PLACEHOLDER?',
        'type':'make_items_question_from_pairs',
        'course_code':'1.1.4',
        'pairs':(
            (('$import sqlite3','$import sqlite3 as sql'), 'access a library to create and connect to a db'),
            (("$conn = sqlite3.connect('hello.db')","$c = sqlite3.connect('hello.db')"), ("create a db file in the same folder as the python file executing the code", "create a file called 'hello.db' if one does not exist", "create a connection to a database file called 'hello.db'")),
            (("$conn = sqlite3.connect('C:\hello.db')", "$c = sqlite3.connect('C:\hello.db')"), ("create a file in the C drive","create a file called 'hello.db' if one does not exist in the C drive", "create a connection to a database file called 'hello.db' located on the C drive")),
            (("$conn = sqlite3.connect(':memory:')", "$c = sqlite3.connect(':memory:')"), ("create a temporary DB file in memory", "create a temporary DB file in RAM")),
            (("$import sqlite", "$import sqlite2"), "raise a module not found error"),
            (("$conn = sqlite.connect(':memory:')", "$conn = sqlite.connect('hello.db')", "$c = sqlite.connect('hello.db')"),'raise a NameError'), 
            (("$connect = sqlite3.conn(':memory:')", "$connect = sqlite.conn('hello.db')", "$c = sqlite.conn('hello.db')"),'raise an AttibuteError'),
            (("$conn = sqlite3.connect(:memory:)", "$conn = sqlite.connect(hello.db)", "$c = sqlite.connect(hello.db)"),'cause a Syntax Error'), 
            ("$c = conn.cursor()","$create a cursor object"),
            ("$conn.commit()", "transfer changes to the database"),
            ("$conn.close()", "end connection with the database")
        ),
        'fillers': (),
    },
    'SQL syntax': {
        'question':"Which of the following are PLACEHOLDER?",
        'positive':'correct',
        'negative':'incorrect',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'course_code':'1.1.5',
        'correct':(
            'not all database systems require a semicolon at the end of each SQL statement',
            'semicolons are commonly used to show the end of an SQL statement',
            'SQL keywords are not case sensitive',
            'SQL keywords are commonly written in upper-case',
            'SQL is not a case sensitive language',
            'table and field names are commonly written in lower-case',
            'two or more SQL statements can be executed in the same call to the server if seperated by semicolons in systems that allow it',
            'most actions performed on databases are done with SQL statements',
            'SQL is case insensitive, but case is used to make it more readable',
            ),
        'incorrect': (
            'all database systems require a semicolon at the end of each SQL statement',
            'SQL keywords are case sensitive',
            'SQL keywords are never written in upper-case',
            'SQL keywords are written in lower-case',
            'SQL is a case sensitive language',
            'table and field names are commonly written in upper-case',
            'table and field names are never written in lower-case',
            'two or more SQL statements can be never be executed in the same call to the server',
            'full stops are commonly used to show the end of an SQL statement',
            'parenthesis are commonly used to show the end of an SQL statement',
            'commas are commonly used to show the end of an SQL statement',
            'dollar signs are commonly used to show the end of an SQL statement',
            'most actions performed on databases are done using python',
            )
        },

    'SQL keywords': {
        'question':"Which of the following is PLACEHOLDER a valid SQL keyword with which to start a statement?",
        'positive':'',
        'negative':'not',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'course_code':'1.1.5',
        'correct':(
            '$SELECT','$UPDATE','$DELETE','$INSERT','$CREATE','$ALTER','$DROP'
            ),
        'incorrect': (
            '$WHERE','$BETWEEN','$AND','$ALL','$BETWEEN','$CHECK','$CONSTRAINT','$DISTINCT','$EXISTS','$FROM','$LIKE','$NOT','$OR','$TABLE','$VALUES','$WHERE'
            )
        },
    'sql commands':sql_commands,
    
    'SQL snippets': {
        'question_with_0':['Which comment would best fit the following code?','PLACEHOLDER'],
        'question_with_1':'Which snippet PLACEHOLDER?',
        'type':'make_items_question_from_pairs',
        'course_code':'1.1.5',
        'pairs':(
            ('$CREATE DATABASE', 'creates a new database'),
            ("$CREATE TABLE", "creates a new table"),
            ("$CREATE INDEX", "creates an index (search key)"),
            ("$SELECT", "extracts data from a database"),
            ("$UPDATE", "updates data in a database"),
            ("$INSERT INTO", "inserts new data into a database"),
            ("$ALTER DATABASE", "modifies a database"),
            ("$ALTER TABLE", "modifies a table"),
            ("$DELETE", "deletes data from a database"),
            ("$DROP TABLE", "deletes a table"),
            ("$DROP INDEX", "deletes an index"),
        ),
        'fillers': (),
    },

    'SQLite3 modules':{
        'question':"Which of the following is PLACEHOLDER a SQLite3 method?",
        'positive':'',
        'negative':'not',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'course_code':'',
        'correct':(
            '$connect', '$cursor', '$commit','$close',
            '$execute','$executemany',
            '$fetchone', '$fetchall'
            ),
        'incorrect': (
            '$disconnect','$makeconnection''$conn','$closeconn',
            '$curse','$cur','$makecursor',
            '$executeone','$executall','$executsome','$executeonebyone',
            '$fetchmany', '$fetchsome','$fetchparse'
            )
    },

    'SQLite3 methods and attributes': {
        'question_with_0':['Which comment would best fit the following code:','PLACEHOLDER'],
        'question_with_1':'Which snippet PLACEHOLDER?',
        'type':'make_items_question_from_pairs',
        'course_code':'1.1.5',
        'pairs':(
            ('$connect', ('creates a connection to a database', 'attempts to create a database if none exists')),
            ("$cursor", ("is a connection object", 'is used to interact with a database')),
            ("$commit", ('is a cursor object',"is a connection object","saves the current transaction", 'if not called, a transaction will not be saved')),
            ("$execute", ('is a cursor object','is a connection object',"executes a valid SQL statement with a given parameter", 'creates a cursor object')),
            ("$executemany", ('is a connection object',"executes valid SQL statement with given parameters", 'creates a cursor object')),
            ("$fetchone", ('is a cursor object',"fetches the next row of a query result set", 'returns none when no more data is available')),
            ("$fetchmany", ('is a cursor object',"returns a list", 'returns an empty list if no more data is vailable', 'returns the number of rows specified')),
            ("$fetchall", ('is a cursor object',"returns a list", 'fetches all rows of a query result','fetches all remaining rows of a query result', 'returns an empty list if no more data is vailable')),
            ("$close", ("is a cursor object",'is a connection object', "closes a cursor object")),
        ),
        'fillers': (),
    },

    'SQLite and Python data types': {
        'question_with_0':['Which SQLITE data type is the equivalent of Python ', 'PLACEHOLDER'],
        'question_with_1':['Which Python datatype best matches the following SQLITE data type?','PLACEHOLDER'],
        'type':'make_items_question_from_pairs',
        'course_code':'1.1.5',
        'pairs':(
            ('$None', '$NULL'),
            ("$int", "$INTEGER"),
            ("$float", '$REAL'),
            ("$str", '$TEXT'),
            ("$bytes", '$BLOB'),
        ),
        'fillers': (
            ('$null', '$NONE'),
            ("$integer", "$NUM"),
            ("$decimal", '$FLOAT'),
            ("$text", '$STRING'),
            ("$bool", '$BOOL'),
        ),
    },


    #################################################################
    'csv modules':{
        'question':"Which of the following is PLACEHOLDER a csv method?",
        'positive':'',
        'negative':'not',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'course_code':'',
        'correct':(
            '$reader', '$writer','$DictWriter', '$DictReader',
            '$writerow','$writerows','$writeheader',
            ),
        'incorrect': (
            '$read', '$write','$WriteDict', '$ReadDict',
            '$writeone','$writemany','$writerall',
            '$writehead','$headwrite',
            )
    },
    
    'sqlite_find_the_line':sqlite_find_the_line,
    'sqlite_outcome':sqlite_outcome,


#################################################################
    'xml.etree.ElementTree code': {
        'question_with_0':['What comment best matches the following code:','PLACEHOLDER'],
        'question_with_1':'Which line of code is best described by PLACEHOLDER?',
        'type':'make_items_question_from_pairs',
        'course_code':'1.1.5',
        'pairs':(
            ("$import xml.etree.ElementTree as ET", ('$import module and define alias')),
            ("$import xml.etree.ElementTree", ('$import module')),
            ("$tree = ET.parse('doc.xml')", ('$create an ElementTree obect from an existing XML document')),
            ("$tree = ET.parse()", ('$create an ElementTree obect')),
            ("$root = tree.getroot()", ('$return the root element from an existing XML document')),
            ("$root = ET.fromstring(xml_data)", ('$return the root element from a string represented by the Element class')),
            ("$root.find('tag').get('attr')", ('$return the first element in root containing a tag named "tag" and display the value of the attribute "attr"')),
        ),
        'fillers': (),
    },
    'XML handling submodules':{
        'question':"Which of the following is PLACEHOLDER a python module for handling XML?",
        'positive':'',
        'negative':'not',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'course_code':'',
        'correct':(
            '$xml.etree.ElementTree', 
            '$xml.dom.minidom','$xml.dom.pulldom',
            '$xml.sax',
            '$xml.parsers.expat',
            ),
        'incorrect': (
            '$xml.etree.Elementry', 
            '$xml.dom.mini','$xml.dom.pushdom',
            '$xml.saxo',
            '$xml.parse.expat',
            '$xml.etree.ElementsTree', 
            '$xml.dom.mdom','$xml.dom.pull',
            '$xml.saxml',
            '$xml.parsers.expatdom',
            '$xml.parsers.dompull',
            '$xml.parsers.domini',
            '$xml.parsers.dommini',
            )
    },
    'xml.etree.ElementTree methods':{
        'question':"Which of the following is PLACEHOLDER a python xml.etree.ElementTree method?",
        'positive':'',
        'negative':'not',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'course_code':'',
        'correct':(
            'parse', 
            'getroot',
            'find','$findall',
            'get',
            'set',
            'remove',
            'Element',
            'SubElement',
            'dump',
            'set',
            'fromstring',

            ),
        'incorrect': (
            'parseall', 
            'findroot',
            'findmany','$findsome'
            'getelement',
            'setelement',
            'removeall',
            'Elements',
            'SubElements',
            'dumpall',
            'put',
            'write',
            'read',
            'fromstr',
            )
        },

    'xml.etree.ElementTree method returns': {
        'question_with_0':['What is the function of the xml.etree.ElementTree method','PLACEHOLDER'],
        'question_with_1':'Which one of the following xml.etree.ElementTree methods PLACEHOLDER?',
        'type':'make_items_question_from_pairs',
        'course_code':'1.1.5',
        'pairs':(
            ("$dump", ('Writes an element tree or element structure to sys.stdout','should be used for debugging only')),
            ("$fromstring", ('parses an XML section from a string constant')),
            ("$fromstringlist", ('parses an XML document from a sequence of string fragments')),
            ("$indent", ('appends whitespace to the subtree to indent the tree visually')),
            ("$iselement", ('checks if an object appears to be a valid element object')),
            ("$iterparse", ('parses an XML section into an element tree incrementally, and reports what???s going on to the user')),
            ("$parse", ('parses an XML section into an element tree')),
            ("$tostring", ("generates a string representation of an XML element, including all subelements")),
            ("$register_namespace", ("Registers a namespace prefix")),
            ("$tostringlist", ("generates a string representation of an XML element, including all subelements")),
            ("$XML", ("parses an XML section from a string constant")),
            ("$XMLID", ("Parses an XML section from a string constant, and also returns a dictionary which maps from element id:s to elements")),
            ("$getroot", ("returns the root element for this tree")),
        ),
        'fillers': (),
    },
    'xml.etree.ElementTree factory function returns': {
        'question_with_0':['What is the function of the xml.etree.ElementTree functions','PLACEHOLDER'],
        'question_with_1':'Which one of the following xml.etree.ElementTree functions PLACEHOLDER?',
        'type':'make_items_question_from_pairs',
        'course_code':'1.1.5',
        'pairs':(
            
            ("$Comment", ("creates a special element that will be serialized as an XML")),
            ("$ProcessingInstruction", ("creates a special element that will be serialized as an XML processing instruction")),
            ("$SubElement", ("creates an element instance, and appends it to an existing element")),
        ),
        'fillers': (
            ("$dump", ('Writes an element tree or element structure to sys.stdout','should be used for debugging only')),
            ("$fromstring", ('parses an XML section from a string constant')),
            ("$fromstringlist", ('parses an XML document from a sequence of string fragments')),
            ("$indent", ('appends whitespace to the subtree to indent the tree visually')),
            ("$iselement", ('checks if an object appears to be a valid element object')),
            ("$iterparse", ('parses an XML section into an element tree incrementally, and reports what???s going on to the user')),
            ("$parse", ('parses an XML section into an element tree')),
            ("$tostring", ("generates a string representation of an XML element, including all subelements")),
            ("$register_namespace", ("Registers a namespace prefix")),
        )
    },
    
    'xml.etree.ElementTree objects': {
        'question_with_0':['Which one of the following exist in this xml.etree.ElementTree object:','PLACEHOLDER'],
        'question_with_1':'Which xml.etree.ElementTree object contains PLACEHOLDER?',
        'type':'make_items_question_from_pairs',
        'course_code':'1.1.5',
        'pairs':(
            ("$Element", ('tag', 'clear()', 'get()', 'items', 'keys()', 'set()', 'append()', 'extend()', 'find()', 'findall()', 'findtext()', 'insert()', 'iter()', 'iterfind()', 'itertext()', 'makeelement()', 'remove()')),
            ("$ElementTree", ('_setroot()', 'find()', 'findall()', 'findtext()','getroot()', 'iter()', 'iterfind()', 'parse()', 'write()')),
            ("$TreeBuilder ", ('close()', 'data()', 'end()', 'start()','comment()', 'doctype()', 'start_ns()', 'end_ns()')),
            ("$XMLParser ", ('close()', 'feed()')),
            ("$XMLPullParser ", ('close()', 'data()', 'read_events()')),
        ),
        'fillers': (
        )
    },
    'XML statements':{
        'question':"Which of the following are PLACEHOLDER correct?",
        'positive':'',
        'negative':'not',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'course_code':'',
        'correct':(
            'stands for extensible markup language', 
            'used for storage of data',
            'used for transmitting data',
            'used for reconstructing data',
            'human readable',
            'machine readable',
            'xml prologs are not essential',
            'xml prologs must come first in the document',
            'xml elements may contain attibutes',
            'each open XML tag must have a corresponding closing tag',
            'all XML documents must have a root element',
            ),
        'incorrect': (
            'stands for extensible mutable language', 
            'stands for expandable markup language', 
            'cannot be used for storage of data',
            'cannot be used for transmitting data',
            'cannot be used for reconstructing data',
            'only used for storage of data',
            'only used for transmitting data',
            'only used for reconstructing data',
            'only human readable',
            'only machine readable',
            'xml prologs are essential',
            'xml prologs can be anywhere in the document',
            'xml elements must contain attibutes',
            'each open XML tag may have a corresponding closing tag',
            'XML documents may have a root element',
            )
        },

################################


    'Log levels': {
        'question_with_0':['Which one of the following log values corresponds to PLACEHOLDER?'],
        'question_with_1':'Which one of the following log level names corresponds to the value PLACEHOLDER?',
        'type':'make_items_question_from_pairs',
        'course_code':'1.1.5',
        'pairs':(
            ("$CRITICAL", ('50')),
            ("$ERROR", ('40')),
            ("$WARNING", ('30')),
            ("$INFO", ('20')),
            ("$DEBUG", ('10')),
            ("$NOTSET", ('0')),
        ),
        'fillers': (
        )
    },

    'log_level_order':log_level_order,





##############################
    'INI files key value entries':{
        'question':"Which of the following are PLACEHOLDER used to separate key/value entries in INI files?",
        'positive':'',
        'negative':'not',
        'type':['multi_option_from_correct_incorrect'],
        'course_code':'',
        'correct':(
            ':', 
            '=',
            ),
        'incorrect': (
            '-', 
            '>', 
            '->',
            '~',
            )
        },
    'INI files comments':{
        'question':"Which of the following are PLACEHOLDER used to create a comment in INI files?",
        'positive':'',
        'negative':'not',
        'type':['multi_option_from_correct_incorrect'],
        'course_code':'',
        'correct':(
            ';', 
            '#',
            ),
        'incorrect': (
            '//', 
            '"', 
            '/>',
            '*/',
            '*',
            )
        },
    
    'INI file syntax': {
        'question_with_0':['Which one of the following are used to PLACEHOLDER in INI files?'],
        'question_with_1':'In INI files, what does the following do: PLACEHOLDER',
        'type':'make_items_question_from_pairs',
        'course_code':'1.1.5',
        'pairs':(
            ("denote a section title", ('[]')),
            ("contain values which may be used by other sections", ('[DEFAULT]')),
            ("create an interpolating value", ('%()\s')),
            ("create a comment", (';', '#')),
            ("seperate a key, value pair", (':', '=')),
        ),
        'fillers': (
        )
    },



}


'''

'question topic':,
'question type':'correct_incorrect',
'question':['with PLACEHOLDER'],
'correct':'',
'incorrect':'',
#if correct, replace with correct, if not replace with incorrect. 


'question topic:',
'question type':'pairs',
'question_with_0':[],#question if item 0 is used in PLACEHOLDER,
'question_with_1':[],#question if item 1 is used in PLACEHOLDER,

views:
def raw_question_to_template_question(raw_question):
    template_question_tup = []
    if type(raw_question) is str():#assume that strings will never just be pure code... I can't think why they would ever be
        template_question_tup.append({'text': raw_question.replace('PLACEHOLDER', indicator)})
    else:
        for line in rawq:
            if raw_question[0] != '$':
                template_question_tup.append({'text': raw_question.replace('PLACEHOLDER', indicator)})
            else:
                template_question_tup.append({'code': raw_question.replace('PLACEHOLDER', indicator)})
    return template_question_tup

template.html:
{% for line in question %}
    {% if line.text is defined %}
        <div class='text'>{{line.text}}</div>
    {% elif line.code is defined %}
        <div class = 'code-container'>
            <pre class="prettyprint">{{line.code}}</pre>
        </div>
    {% endif %}
{% endfor %}

Common commands
    
Syntax
    statements
    patterns
    examples of each keywords
    create
    read
    update
    delete
'''