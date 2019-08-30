work_dir = e_python.Dir('.')


ld_abspath = path.join(
    work_dir.abspath,
    'install',
    'usr/local',
    'lib'),

_builder_python_env = {
    "LD_LIBRARY_PATH" : Libs['python'].ld_abspath,
}

_builder_python_env_str = " ".join(
    map(lambda k: k + "=" + _builder_python_env[k],
        _builder_python_env.keys())
)

_builder_python_env_str = "_LD_LIBRARY_PATH="







'/usr/local/bin/python'

action = Action(
    # Run _builder_python prefixed with any needed environment settings.
    _builder_python_env_str + " " + _builder_python \
     " -m compileall -q -d ${SOURCE.path} -f ${SOURCE.abspath} " \
     " && if [ -x ${SOURCE.abspath} ]; then " \
     "       chmod a+x ${TARGET.abspath}; " \
     "fi",
    "" if e_build['VERBOSE'] else "pyc      ${TARGET}"
    ),