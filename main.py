from io import BytesIO
import sys
from time import sleep
from typing import Union
from datetime import datetime, date as Date

from tfprotocol_client import (
    FileStatTypeEnum,
    KeepAliveMechanismType,
    KeepAliveOptions,
    PutGetCommandEnum,
    StatusInfo,
    TfProtocol,
    TransferStatus,
    CodesSenderRecvr,
    ProtocolClient,
    TfProtoHandler,
)
from tfprotocol_client.misc.file_stat import FileStat


def get_publickey():
    """[summary]

    Returns:
        [type]: [description]
    """
    with open('public.key', mode='r', encoding='utf8') as f:
        public_key = f.read()
    return public_key


class MyHandler(TfProtoHandler):
    """My handler

    Args:
        SuperProtoHandler ([type]): [description]
    """

    def mkdir_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def ftod_callback(self, timestamp: int, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            'timestamp:(',
            timestamp,
            ')',
        )

    def datef_callback(self, date: datetime, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            'date:(',
            date,
            ')',
        )

    def del_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def rmdir_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def copy_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def touch_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def fupd_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            status.payload,
        )

    def date_callback(self, timestamp: int, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            'timestamp:(',
            timestamp,
            ')',
            status.status.name.ljust(8, ' '),
        )

    def dtof_callback(self, date: Date, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def fstat_callback(self, filestat: FileStatTypeEnum, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            status.payload,
        )

    def cpdir_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def xcopy_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def xdel_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def xrmdir_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def xcpdir_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def lock_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def sendfile_callback(
        self,
        is_overriten: bool,
        path: str,
        status: StatusInfo,
        payload: Union[bytes, bytearray],
    ):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def rcvfile_callback(
        self, delete_after: bool, path: str, status: StatusInfo, sink: BytesIO = None
    ):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            len(status.payload),
            sep=' ',
        )
        # if len(status.payload) > 21588:
        #     print('-------')
        #     print(status.payload)
        #     print('-------')
        if sink is None:
            print(
                "CLIENT-HANDLER: ",
                sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
                status.status.name.ljust(8, ' '),
                ' ',
                'NO-SINK-PASSED',
            )
            return
        if sink.writable() and status.payload:
            sink.write(status.payload)

    def ls_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def lsr_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            status.message,
        )

    def renam_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def keepalive_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def login_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def chmod_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            status.payload,
        )

    def chown_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def getcan_callback(
        self,
        status: StatusInfo,
        client: ProtocolClient,
        transfer_status: TransferStatus,
    ):
        if transfer_status is not None:
            if transfer_status.dummy_state:
                # transfer_status.dummy = PutGetCommandEnum.HPFCANCEL.value
                pass
            elif transfer_status.dummy in (
                PutGetCommandEnum.HPFCANCEL.value,
                PutGetCommandEnum.HPFEND.value,
            ):
                print(
                    "CLIENT-HANDLER: ",
                    sys._getframe()
                    .f_code.co_name.removesuffix('_callback')
                    .ljust(10, ' '),
                    '-'.ljust(8, '-'),
                    'finished',
                )
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' ')
            if status is not None
            else '-'.ljust(8, '-'),
            transfer_status,
        )

    def putcan_callback(
        self,
        status: StatusInfo,
        client: ProtocolClient,
        transfer_status: TransferStatus,
    ):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' ')
            if status is not None
            else '-'.ljust(8, '-'),
            transfer_status,
        )

    def sha256_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            status.payload,
        )

    def prockey_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            status.payload,
        )

    def freesp_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def udate_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def ndate_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def getstatus_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            status.code,
        )

    def get_callback(self, codes: CodesSenderRecvr):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            codes.last_header,
        )
        # sleep(0.3)
        # codes.send_get(PutGetCommandEnum.HPFCANCEL.value)

    def put_callback(self, codes: CodesSenderRecvr):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            '-'.ljust(8, '-'),
            codes.last_header,
        )

    def putstatus_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def nigma_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            'NewSessionKey:(',
            status.payload,
            ')',
        )

    def rmsecuredirectory_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def injail_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def tlb_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def sdown_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def sup_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def fsize_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            status.code,
        )

    def fsizels_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            status.code,
        )

    def lsv2_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def lsrv2_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def ftype_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            status.payload,
        )

    def ftypels_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
            status.payload,
        )

    def fstatls_callback(self, file_stat: FileStat):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            '-'.ljust(8, '-'),
            file_stat,
        )

    def echo_callback(self, value: str):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            '-'.ljust(8, ' '),
            'ServerSays:("',
            value,
            '")',
        )
        print(f'Server: {value}')

    def status_server(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def response_server_callback(self, status: StatusInfo):
        print(
            "CLIENT-HANDLER: ",
            sys._getframe().f_code.co_name.removesuffix('_callback').ljust(10, ' '),
            status.status.name.ljust(8, ' '),
        )

    def instance_tfprotocol(self, instance: any):
        print(
            "CLIENT-HANDLER: ", sys._getframe().f_code.co_name.removesuffix('_callback')
        )


def test_updown_tinyfiles(proto: TfProtocol):
    # DONE
    with open('test2.java', 'rb') as f:
        proto.sendfile_command(True, 'test2.java', f)

    with open('test2-rec.java', 'wb') as f:
        proto.rcvfile_command(False, 'test2.java', f)

    proto.fstat_command('test2.java')


def test_supsdown_files(proto: TfProtocol):
    # DONE
    with open('test2.java', 'rb') as f:
        proto.sup_command('test2.2.java', f, 5)

    with open('test2.2-rec.java', 'wb') as f:
        proto.sdown_command('test2.2.java', f, 10)

    proto.fstat_command('test2.2.java')


def test_putcangetcan_files(proto: TfProtocol):
    # DONE
    with open('test2.java', 'rb') as f:
        proto.putcan_command(f, 'test2.3.java', 0, 1024, 1)

    with open('test2.3-rec.java', 'wb') as f:
        proto.getcan_command(f, 'test2.3.java', 0, 1024, 2)

    proto.fstat_command('test2.3.java')


def test_putget_files(proto: TfProtocol):
    # DONE
    with open('test2.java', 'rb') as f:
        proto.put_command(f, 'test2.4.java', 0, 48)

    with open('test2.4-rec.java', 'wb') as f:
        proto.get_command(f, 'test2.4.java', 0, 48)

    proto.fstat_command('test2.4.java')


def test_folders_commands(proto: TfProtocol):
    # DONE
    proto.rmdir_command('leo_test')

    proto.mkdir_command('leo_test')
    proto.mkdir_command('leo_test/pattern')
    proto.mkdir_command('leo_test/214pattern')
    proto.mkdir_command('leo_test/test1')
    proto.mkdir_command('leo_test/test2')
    proto.touch_command('leo_test/test2/test.java')
    proto.mkdir_command('leo_test/test2/test21')
    proto.mkdir_command('leo_test/test2/test22')
    proto.mkdir_command('leo_test/test3')

    proto.lsr_command('/leo_test')

    proto.renam_command('/leo_test/test3', '/leo_test/test3new')
    proto.lsr_command('/leo_test')

    proto.cpdir_command('/leo_test/test2', '/leo_test/test2cpdir')
    proto.lsr_command('/leo_test')

    proto.xcpdir_command('testxcpdir', '/leo_test/test2', 'pattern')
    proto.lsr_command('/leo_test')

    proto.mkdir_command('/leo_test/test2copy')
    proto.copy_command('leo_test/test2/test.java', 'leo_test/test2copy/test.java')
    proto.lsr_command('/leo_test')

    proto.mkdir_command('/leo_test/test2xcopy')
    # how to use this command
    proto.xcopy_command(
        'test_xcopy.java', '/leo_test/test2copy/test.java', 'test21',
    )
    proto.lsr_command('/leo_test')

    proto.xdel_command('/leo_test', 'test.java')
    proto.lsr_command('/leo_test')

    proto.xrmdir_command('/leo_test', 'test2')
    proto.lsr_command('/leo_test')

    proto.touch_command('/leo_test/file_touch.txt')
    proto.lsr_command('/leo_test')

    proto.lsrv2_command('/leo_test', '/leo_test/testrls.txt')

    proto.lsv2_command('/leo_test', '/leo_test/testls.txt')

    proto.fsize_command('/leo_test/testls.txt')

    proto.fsizels_command('/leo_test/testls.txt')


def test_files_modification_commands(proto: TfProtocol):
    proto.rmdir_command('/leo_test')

    proto.mkdir_command('/leo_test')
    proto.touch_command('/leo_test/file_touch.txt')
    proto.fstat_command('/leo_test/file_touch.txt')

    proto.chmod_command('/leo_test/file_touch.txt', '600')
    proto.fstat_command('/leo_test/file_touch.txt')

    # proto.chown_command('/leo_test/file_touch.txt', '', '')
    # proto.fstat_command('/leo_test/file_touch.txt')

    proto.fupd_command('/leo_test/file_touch.txt')
    proto.fstat_command('/leo_test/file_touch.txt')


def test_regular_commands(proto: TfProtocol):
    proto.echo_command('Hola mundo')

    # proto.nigma_command(KEY_LEN_INTERVAL[1])
    proto.echo_command('Hola despues de cambiar el cerrojo')
    proto.date_command()
    proto.datef_command()
    proto.dtof_command(datetime.timestamp(datetime.now()))
    proto.ftod_command('1999-12-10 12:12:0')
    proto.udate_command()
    proto.freesp_command()
    proto.prockey_command()
    proto.sha256_command('test2.java')

    proto.end_command()


def main():
    ADDRESS = '192.168.0.125'
    # ADDRESS = 'tfproto.expresscuba.com'
    PORT = 10345
    proto = TfProtocol(
        '0.0',
        get_publickey(),
        'testhash',
        MyHandler(),
        ADDRESS,
        PORT,
        verbosity_mode=True,
    )

    proto.connect(
        keepalive_options=KeepAliveOptions(
            KeepAliveMechanismType.UDP_HOSTCHECK, 1, 5, 3
        )
    )
    proto.echo_command('dime que?')
    sleep(20)
    proto.echo_command('a dormir')
    # test_updown_tinyfiles(proto)
    # test_supsdown_files(proto)
    # test_putget_files(proto)
    # test_putcangetcan_files(proto)
    # test_folders_commands(proto)
    # test_files_modification_commands(proto)
    # test_regular_commands(proto)

    # proto.rmdir_command('prueba.sd')
    # proto.tlb_command()


if __name__ == '__main__':
    main()
