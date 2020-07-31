from web_server_validator import WebServerValidator
import settings


def main():
    try:
        web_server_validator = WebServerValidator(settings.WEB_SERVER_IP)
        web_server_validator.is_server_ok()
        web_server_validator.is_content_valid()
        print('Ran all tests successfully')

    except Exception as e:
        print('Server is not valid')
        raise e


if __name__ == '__main__':
    main()
