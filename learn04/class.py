class Entity:
    def __init__(self, object_type):
        print("parent Entity created")
        self.object_type = object_type
    def get_context_length(self):
        raise NotImplementedError
    def print_title(self):
        print(self.title)

class Document(Entity):
    def __init__(self, title, author, context):
        print("Document created")
        Entity.__init__(self, "document")
        self.title = title
        self.author = author
        self.__context = context
    def get_context_length(self):
        return len(self.__context)

class Video(Entity):
    def __init__(self, title, author, video_context):
        print("Video created")
        Entity.__init__(self, "video")
        self.title = title
        self.author = author
        self.__video_context = video_context
    def get_context_length(self):
        return len(self.__video_context)

harry = Document("Harry Potter", "J.K.Rowling", "Harry Potter is a novel by J.K.Rowling")
harry_movie = Video("Harry Potter Movie", "J.K.Rowling", "Harry Potter Movie is a movie by J.K.Rowling")

print(harry.object_type)
print(harry_movie.object_type)


print(harry.get_context_length())
print(harry_movie.get_context_length())

harry.print_title()
harry_movie.print_title()
