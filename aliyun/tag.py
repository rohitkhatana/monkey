from config import TAG_KEY_VALUE

class Tag:

    def _find_by_tag_name(self, key, tags):
        return filter(lambda tag: tag['TagKey'] == key, tags)

    def _valid_tag_value(self, key, cloud_tag_object):
        return cloud_tag_object.get('TagValue') in TAG_KEY_VALUE[key].get('value', list())

    def _msg(self, key):
        return {
                'valid': False,
                'msg': '{} tag is missing or invalid value. Supported values: {}'.format(key, ','.join(TAG_KEY_VALUE[key].get('value', '')))
        }

    def validate_tags(self, tags):
        invalid_tags = []
        for key, value in TAG_KEY_VALUE.items():
            tag = self._find_by_tag_name(key, tags)
            if value.get('required', None) and not tag:
                invalid_tags.append(self._msg(key))
            elif tag and not self._valid_tag_value(key, tag[0]):
                invalid_tags.append(self._msg(key))
        return invalid_tags

