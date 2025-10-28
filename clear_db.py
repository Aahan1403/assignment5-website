from DAL import get_connection

if __name__ == '__main__':
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM projects')
    conn.commit()
    cur.execute('SELECT COUNT(*) FROM projects')
    count = cur.fetchone()[0]
    conn.close()
    print('Rows remaining in projects:', count)
