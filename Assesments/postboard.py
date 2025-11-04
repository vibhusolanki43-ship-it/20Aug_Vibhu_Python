import datetime

users = []
posts = []
def register():
    username = input("Enter new username: ").strip()
    if not username:
        print(" Username cannot be empty.")
        return
    if username in users:
        print("Username already exists. Try another.")
        return
    password = input("Enter password: ").strip()
    if not password:
        print(" Password cannot be empty.")
        return
    users[username] = password
    print(f" User '{username}' registered successfully!")

def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if username in users and users[username] == password:
        print(f" Welcome {username}!")
        return username
    else:
        print(" Invalid credentials. Try again.")
        return None

def create_post(username):
    title = input("Enter Post Title: ").strip()
    if not title:
        print(" Title cannot be empty.")
        return
    desc = input("Enter Post Description: ").strip()
    if not desc:
        print(" Description cannot be empty.")
        return
    
    date_choice = input("Auto date? (Y/N): ").strip().lower()
    if date_choice == 'n':
        date = input("Enter Date (YYYY-MM-DD): ").strip()
    else:
        date = datetime.datetime.now().strftime("%Y-%m-%d")

    post = {
        "author": username,
        "title": title,
        "description": desc,
        "date": date
    }
    posts.append(post)
    print(" Post created successfully!")

def view_posts():
    if not posts:
        print(" No posts yet.")
        return
    print("\n===== ALL POSTS =====")
    for i, post in enumerate(posts, start=1):
        print(f"\nPost #{i}")
        print(f" Author: {post['author']}")
        print(f" Date: {post['date']}")
        print(f" Title: {post['title']}")
        print(f" Description: {post['description']}")

def search_by_user():
    username = input("Enter username to search: ").strip()
    user_posts = [p for p in posts if p['author'] == username]
    if not user_posts:
        print(" No posts found for this user.")
        return
    print(f"\n===== Posts by {username} =====")
    for post in user_posts:
        print(f"\n {post['date']} |  {post['title']}\n {post['description']}")


def main_menu():
    while True:
        print("\n=== PostBoard ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            register()
        elif choice == '2':
            user = login()
            if user:
                user_menu(user)
        elif choice == '3':
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

def user_menu(username):
    while True:
        print(f"\n=== Welcome, {username}! ===")
        print("1. Create Post")
        print("2. View All Posts")
        print("3. Search Posts by Username")
        print("4. Logout")
        choice = input("Enter choice: ").strip()
        
        if choice == '1':
            create_post(username)
        elif choice == '2':
            view_posts()
        elif choice == '3':
            search_by_user()
        elif choice == '4':
            print(" Logged out.")
            break
        else:
            print(" Invalid choice.")

if __name__ == "__main__":
    main_menu()
