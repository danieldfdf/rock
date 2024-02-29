# member class 정의
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    # 회원 정보 프린트
    def display(self):
        print(f"Name: {self.name}, Username: {self.username}")

# post class 정의
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

# 회원 인스턴스 생성 및 append를 써서 리스트에 저장
members = []
members.append(Member("aaaaaaaa", "11111111", "99999999"))
members.append(Member("bbbbbbbb", "22222222", "88888888"))
members.append(Member("cccccccc", "33333333", "77777777"))

# members 리스트를 돌며 회원들의 이름 프린트
for member in members:
    member.display()

# 각 회원별로 게시글 생성 (posts를 사용 빈자리에 append 사용해서 저장)
posts = []
posts.append(Post("a first post", "This is a first post", "aaaaaaaa"))
posts.append(Post("a second post", "This is a second post", "aaaaaaaa"))
posts.append(Post("a third post", "This is a third post", "aaaaaaaa"))

posts.append(Post("b first post", "This is b first post", "bbbbbbbb"))
posts.append(Post("b second post", "This is b second post", "bbbbbbbb"))
posts.append(Post("b third post", "This is b third post", "bbbbbbbb"))

posts.append(Post("c first post", "This is c first post", "cccccccc"))
posts.append(Post("c second post", "This is c second post", "cccccccc"))
posts.append(Post("c third post", "This is c third post", "cccccccc"))

# 특정 유저가 작성한 게시글의 제목 프린트
specific_user = "aaaaaaaa"
print(f"\nPosts by {specific_user}:")
for post in posts:
    if post.author == specific_user:
        print(post.title)

specific_user = "bbbbbbbb"
print(f"\nPosts by {specific_user}:")
for post in posts:
    if post.author == specific_user:
        print(post.title)


specific_user = "cccccccc"
print(f"\nPosts by {specific_user}:")
for post in posts:
    if post.author == specific_user:
        print(post.title)


# 특정 단어가 content에 포함된 게시글의 제목 프린트
specific_word = "second"
print(f"\nPosts containing '{specific_word}':")
for post in posts:
    if specific_word in post.content:
        print(post.title)
