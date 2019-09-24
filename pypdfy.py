
import re

class Pypdfy:
    def __init__(self):

        self.image = 0
        self.is_path = True
        self.not_image = 0
        self.options = {
            'statistics' : False
        }

    def is_image(self, file):

        if self.is_path:
            file_contents = open(file, 'rb').read()
        else:
            file_contents = file

        pages_1 = re.findall(b'(/Page)[^s]+', file_contents)
        bits_per_component_1 = re.findall(b'/BitsPerComponent', file_contents)

        pages_1 = [str(i) for i in pages_1]
        bits_per_component_1 = [str(i) for i in bits_per_component_1]

        page_match = "b\'/Page\'"
        pages = [i for i in pages_1 if i == page_match]

        #Is image
        if len(bits_per_component_1) == len(pages):
            return True
        # Is not image
        else:
            return False

    def are_images(self, files, **options):
        for i in options:
            self.options[i] = options[i]

        get_images = [self.is_image(i) for i in files]
        results = dict(results=get_images) if len(options) > 0 else get_images

        if self.options['statistics']:
            results['statistics'] = self.statistics(results['results'])

        return results

    def statistics(self, results):
        self.total_files = len(results)
        for i in results:
            if i:
                self.image += 1
            else:
                self.not_image += 1

        not_img_stat = round((self.not_image/self.total_files)*100)
        is_img_stat = round((self.image/self.total_files)*100)
        stats_results = (not_img_stat, is_img_stat)

        return stats_results