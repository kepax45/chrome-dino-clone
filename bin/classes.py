import pygame

def load_img(path):
    return pygame.image.load(path)
def scaled(image, width, height):
    return pygame.transform.scale(image, (width, height))
def rotated(image, angle):
    return pygame.transform.rotate(image, angle)
class Object:
    def update_transform(self, x=None, y=None, width=None, height=None):
        if(x!=None):
            self.x = x
        if(y!=None):
            self.y = y
        if(width!=None):
            self.width = width
        if(height!=None):
            self.height = height
    def __init__(self, x, y, width, height, clusters=None):
        self.clusters = []
        self.main_img = None
        if(clusters!=None):
            self.clusters = clusters
            self.main_img = self.clusters[0].images[0]
        self.update_transform(x, y, width, height)
    def adjust_transform(self):
        self.update_transform(width=self.main_img.get_width(), height=self.main_img.get_height())
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    def endpointX(self):
        return self.x + self.width
    def endpointY(self):
        return self.y + self.height
    def add_cluster(self, cluster):
        self.clusters.append(cluster)
    def find_image(self, label):
        for cluster in self.clusters:
            for image in cluster.images:
                if label==image.label:
                    return image
        return -1
    def collides(self, obj1):
        return self.get_rect().colliderect(obj1.get_rect())
    def collides_point(self, p):
        return p[0]>=self.x and p[0]<=self.endpointX() and p[1]>=self.y and p[1]<=self.endpointY()
    def find_cluster(self, label):
        for cluster in self.clusters:
            if cluster.label==label:
                return cluster
        return -1
    def change_image(self, label):
        image = self.find_image(label)
        if(image!=-1):
            self.main_img = image
    def force_image(self, image):
        self.main_img = image
    def draw(self, surface):
        surface.blit(self.main_img, (self.x, self.y))
    def animate(self, cluster_label):
        cluster =  self.find_cluster(cluster_label)
        self.main_img = cluster.get_image()
        cluster.shift_image()
class Image:
    def __init__(self, label, path):
        if(type(path)==type("")):
            self.img = pygame.image.load(path)
        else:
            self.img = path
        self.label = label
class Cluster:
    def __init__(self, label, images):
        self.counter = 0
        self.images = images
        self.label = label
    def __count(self):
        self.counter = (self.counter+1)%len(self.images)
    def get_image(self):
        return self.images[self.counter]
    def add_image(self, image):
        self.images.append(image)
    def add_images(self, images):
        self.images += images
    def shift_image(self):
        self.__count()
