class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        filter_album = [album for album in self.albums if album.name == album_name]
        if not filter_album:
            return f"Album {album_name} is not found."
        current_album = filter_album[0]
        if current_album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(current_album)
        return f"Album {current_album.name} has been removed."

    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += album.details()
        return result
