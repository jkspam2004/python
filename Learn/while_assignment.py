def get_users():
    return True

count = 0
while True:
    result = get_users()
    print result
    count += 1
    if count > 9:
        break
    

""" in Python, cannot assign a variable in while loop like in Perl below
use a while True and assign variable inside and break when the condition is false
sub get_user {
    return True;
}

my $count = 0;
while (my $val = get_user()) {
    print $val, "\n";
    $count++;
    last if $count > 3;
}
"""
