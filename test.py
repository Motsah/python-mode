synchro_plan = [
    SYNCHROPlan(
        name='Truc',
        template=None,
        remote_file=None,
        cmd='echo Truc',
        expected=(
            SmartDict(
                name='ntfp1',
                vrfid=0,
                master=None,
                port=0,
                type='ether',
                flags=[
                    dumpjson.IFF_UP,
                    dumpjson.IFF_RUNNING,
                    dumpjson.IFF_FWD4,
                    dumpjson.IFF_FWD6,
                ]
            ),
        ),
        plan={
        },
    ),
]

        return synchro_plan
