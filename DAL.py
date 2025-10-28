import sqlite3
from sqlite3 import Connection
from typing import List, Dict, Optional

DB_PATH = 'projects.db'

def get_connection() -> Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db() -> None:
    """Create the projects table if it doesn't exist."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            imagefilename TEXT
        )
        '''
    )
    conn.commit()
    conn.close()

def get_projects() -> List[Dict]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, title, description, imagefilename FROM projects ORDER BY id DESC')
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def add_project(title: str, description: str, imagefilename: Optional[str] = None) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO projects (title, description, imagefilename) VALUES (?, ?, ?)',
                (title, description, imagefilename))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id

def get_project(project_id: int) -> Optional[Dict]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, title, description, imagefilename FROM projects WHERE id = ?', (project_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None
