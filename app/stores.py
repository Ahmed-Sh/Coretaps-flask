import itertools, copy

class BaseStore:

    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self, item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_by_id(self, id):
        all_instances = self.get_all()
        result = None
        for instance in all_instances:
            if instance.id == id:
                result = instance
                break
        return result

    def update(self, instance):
        result = instance
        all_instances = self.get_all()

        for index, current_instance in enumerate(all_instances):
            if current_instance.id == instance.id:
                all_instances[index] = instance
                break
        return result

    def delete(self, id):
        instance =  self.get_by_id(id)
        self._data_provider.remove(instance)


    def entity_exists(self, instance):
        result = True
        if self.get_by_id(instance.id) is None:
            result = False
        return result




class MemberStore(BaseStore):
    members = []
    last_id = 1

    def __init__(self):
        super().__init__(MemberStore.members, MemberStore.last_id)


    def get_by_name(self, name):
        return (member for member in self.get_all() if member.name == name)

    def get_members_with_posts(self, all_posts):
        all_members = copy.deepcopy(self.get_all())

        for member, post in itertools.product(all_members, all_posts):
            if member.id == post.member_id:
                member.posts.append(post)

        for member in all_members :
            yield member

    def get_top_two(self, all_posts):
        members_with_posts = list(self.get_members_with_posts(all_posts))

        members_with_posts.sort(key=lambda member: len(member.posts), reverse=True)

        yield members_with_posts[0]
        yield members_with_posts[1]


class PostsStore(BaseStore):
    posts = []
    last_id = 1

    def __init__(self):
        super().__init__(PostsStore.posts, PostsStore.last_id)

    def get_posts_by_date(self):
        all_posts = self.get_all()
        all_posts.sort(key=lambda post: post.date, reverse=True)
        return (post for post in all_posts)

    def get_by_name(self, title):
        all_posts = self.get_all()
        for post in all_posts:
            if post.title == title:
                yield post
