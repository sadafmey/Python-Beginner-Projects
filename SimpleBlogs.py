import os
import datetime

ARTICLES_DIR = "articles"

def write_article(title, author, content):
    """Write a new article to a file. Because every great blog post begins with a blank page and a cup of imagination!"""
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"{timestamp}.txt"
    filepath = os.path.join(ARTICLES_DIR, filename)
    with open(filepath, "w") as f:
        f.write(f"Title: {title}\n")
        f.write(f"Author: {author}\n")
        f.write(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(content)
    print("Article published successfully! Your words are now immortalized in the digital ether.")

def list_articles():
    """List all articles. Because in the grand library of blog posts, every article is a gem waiting to be discovered."""
    print("List of Articles:")
    articles = os.listdir(ARTICLES_DIR)
    for article in articles:
        print(article)

def read_article(filename):
    """Read an article from a file. Dive into the digital pages of your favorite blog post and let the words whisk you away on an adventure!"""
    filepath = os.path.join(ARTICLES_DIR, filename)
    with open(filepath, "r") as f:
        print(f.read())

def main():
    """Main function to interact with the blog engine. Welcome to the digital realm of creativity and cat memes!"""
    print("Welcome to Simple Blog Engine!")

    while True:
        print("\nMenu:")
        print("1. Write Article")
        print("2. List Articles")
        print("3. Read Article")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            title = input("Enter the title of the article: ")
            author = input("Enter your name: ")
            content = input("Enter the content of the article: ")
            write_article(title, author, content)
        elif choice == '2':
            list_articles()
        elif choice == '3':
            filename = input("Enter the filename of the article you want to read: ")
            read_article(filename)
        elif choice == '4':
            print("Thank you for using Simple Blog Engine. May your words be as boundless as your creativity!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4. Remember, there are no wrong choices in the world of blogging!")

if __name__ == "__main__":
    if not os.path.exists(ARTICLES_DIR):
        os.makedirs(ARTICLES_DIR)
    main()
