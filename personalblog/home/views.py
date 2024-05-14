from django.shortcuts import render
from datetime import date

list_posts = [
    {
        "slug":"bible",
        "title": "Benefit of Reading the Bible",
        "image": "bible.jpg",
        "author": "Jethro",
        "date": date.today(),
        "content": """
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Culpa quae velit inventore vitae, cupiditate reprehenderit minus earum eveniet necessitatibus ducimus 
        minima quos laborum dolor vero labore exercitationem, architecto facere adipisci.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Culpa quae velit inventore vitae, cupiditate reprehenderit minus earum eveniet necessitatibus ducimus minima 
        quos laborum dolor vero labore exercitationem, architecto facere adipisci.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Culpa quae velit inventore vitae, cupiditate reprehenderit minus earum eveniet necessitatibus ducimus minima 
        quos laborum dolor vero labore exercitationem, architecto facere adipisci.
                """
    },{
         "slug":"programming",
        "title": "programming is fun?",
        "image": "programming.jpg",
        "author": "Jethro",
        "date": date.today(),
        "content": """
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Culpa quae velit inventore vitae, cupiditate reprehenderit minus earum eveniet necessitatibus ducimus 
        minima quos laborum dolor vero labore exercitationem, architecto facere adipisci.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Culpa quae velit inventore vitae, cupiditate reprehenderit minus earum eveniet necessitatibus ducimus minima 
        quos laborum dolor vero labore exercitationem, architecto facere adipisci.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Culpa quae velit inventore vitae, cupiditate reprehenderit minus earum eveniet necessitatibus ducimus minima 
        quos laborum dolor vero labore exercitationem, architecto facere adipisci.
                """
    },{
        "slug":"exercise",
        "title": "Exercise: Discipline is the key",
        "image": "exercise.jpg",
        "author": "Jethro",
        "date": date.today(),
        "content": """
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Culpa quae velit inventore vitae, cupiditate reprehenderit minus earum eveniet necessitatibus ducimus 
        minima quos laborum dolor vero labore exercitationem, architecto facere adipisci.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Culpa quae velit inventore vitae, cupiditate reprehenderit minus earum eveniet necessitatibus ducimus minima 
        quos laborum dolor vero labore exercitationem, architecto facere adipisci.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Culpa quae velit inventore vitae, cupiditate reprehenderit minus earum eveniet necessitatibus ducimus minima 
        quos laborum dolor vero labore exercitationem, architecto facere adipisci.
                """
    }
]

def get_date(post):
    return post['date']

def home(request):
    sorted_post = sorted(list_posts, key=get_date)
    latest_post = sorted_post[-3:]
    return render(request, "home/home.html", {
        "posts": latest_post
    })

def post(request, slug):  
    return render(request, "home/post-page.html")