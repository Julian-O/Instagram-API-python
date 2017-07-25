from InstagramAPI import InstagramAPI, credentials
API = InstagramAPI(credentials.USERNAME, credentials.PASSWORD)


def main():
    API.login()  # login
    media_id = '1469246128528859784_1520706701'  # a media_id
    # array of user_ids. They can be strings or ints
    recipients = []
    API.direct_share(media_id, recipients, text='This is the last one.')


if __name__ == '__main__':
    main()
