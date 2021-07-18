class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        result = ''
        for document in self.documents:
            result = f"{document}\n"
        return result

    @staticmethod
    def is_object_in_list(obj, list_of_obj):
        return obj in list_of_obj

    @staticmethod
    def get_object(obj_id, list_of_obj):
        return [obj for obj in list_of_obj if obj.id == obj_id][0]

    def add_category(self, category):
        if not self.is_object_in_list(category, self.categories):
            self.categories.append(category)

    def add_topic(self, topic):
        if not self.is_object_in_list(topic, self.topics):
            self.topics.append(topic)

    def add_document(self, document):
        if not self.is_object_in_list(document, self.documents):
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.get_object(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.get_object(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.get_object(document_id, self.documents)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.get_object(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.get_object(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.get_object(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.get_object(document_id, self.documents)
        return document
