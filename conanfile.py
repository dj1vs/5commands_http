from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout

class FiveComamndsHttp(ConanFile):
    name = "FiveCommandsHttp"
    version = "0.0.1"

    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("oatpp/1.3.0.latest")

    def imports(self):
        # copy downloaded/builded protoc and grpc bin
        # used by gen_proto_api.sh script
        self.copy("license*",dst="licenses", folder=True, ignore_case=True)
        self.copy('*.so*', dst='lib', src='lib')

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tool = CMakeToolchain(self)
        tool.generate()

    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    
    def package(self):
        cmake = CMake(self)
        cmake.install()