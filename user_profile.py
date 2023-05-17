def build_profile(first, last, **user_info):
    """Build a dictionary containing everythin we know about a user"""

    user_info['first_name'] = first
    user_info['las_name'] = last
    return user_info

user_profile = build_profile('eduardo', 'blanco', location='bogotá', field='philosophy', age=29, nationality='venezuelan')

print(user_profile)