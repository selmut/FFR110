def ddiff_eqn(prev_row, new_row, prev_col, new_col, current):
    return prev_row+prev_col+new_row+new_col-4*current


def diff_u_eqn(a, b, u, v, Du, ddiff):
    return a-(b+1)*u + (u**2)*v + Du*ddiff


def diff_v_eqn(b, u, v, Dv, ddiff):
    return b*u-(u**2)*v+Dv*ddiff


def euler_fwd(old, diff, h):
    return old+diff*h