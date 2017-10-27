import crayons
import subprocess


def add_signature(func):
    def wrapper(msg=''):
        if not msg:
            return func(msg)
        else:
            return func('[*] %s' % msg)

    return wrapper


@add_signature
def success(msg):
    print(crayons.green(msg, bold=True))


@add_signature
def info(msg):
    print(crayons.white(msg, bold=True))


@add_signature
def error(msg):
    print(crayons.red(msg, bold=True))


@add_signature
def debug(msg):
    print(crayons.blue(msg, bold=False))


def exec_command(
    cmd,
    pre_func=lambda: None,
    except_func=lambda: None,
    else_func=lambda: None,
    finally_func=lambda: None,
    suppress_output=False,
):
    pre_func()

    try:
        if not suppress_output:
            print(subprocess.check_output(cmd))
    except subprocess.CalledProcessError, e:
        print("Terraform command error:\n", e.output)
        except_func()
    else:
        else_func()
    finally:
        finally_func()
