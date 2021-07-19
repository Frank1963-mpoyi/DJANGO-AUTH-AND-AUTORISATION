def input_get_input(self):
    
    _i   = self.request.GET
    user = self.request.user

    i = {
        'user'          : user,
        'user_fullname' : user.fullname,
    }

    return i


def input_post_input(self):# with self it the the place of method , if function it request inside

    _i   = self.request.POST
    user = self.request.user

    i = {
        'user'         : user,
        'user_fullname': user.fullname,

        'title'         : _i.get('title', ''),
        'assigned_to'   : _i.get('assigned_to', ''),
        'assigned_by'   : user,
        'description'   : _i.get('description', ''),
        'dev_note'      : _i.get('dev_note', ''),
        'language'      : _i.get('language', 'FR'),
        'type'          : _i.get('type', 2),
        'status'        : _i.get('status', ''),

        'prev_status'   : _i.get('prev_status', ''),
        'curr_status'   : _i.get('curr_status', ''),
        'operation'     : 'C',
    }

    return i
