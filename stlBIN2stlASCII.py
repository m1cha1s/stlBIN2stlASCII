from struct import unpack
from sys import argv

def main():
    triangles = [] # List of triangles

    with open(argv[1], "rb") as stl:
        stl.seek(80) # Skipping header

        triangleCount = unpack("<i", stl.read(4))[0] # Triangle count
        
        for _ in range(triangleCount):
            triangles.append(unpack("<ffffffffffffH", stl.read(50))) # Decoding triangles
        
    with open(argv[2], "w") as stl:
        
        stl.write("solid ASCII\n")
        
        for triangle in triangles:
            stl.write("  facet normal {} {} {}\n".format(triangle[0], triangle[1], triangle[2]))
            stl.write("    outer loop\n")
            stl.write("      vertex   {} {} {}\n".format(triangle[3], triangle[4], triangle[5]))
            stl.write("      vertex   {} {} {}\n".format(triangle[6], triangle[7], triangle[8]))
            stl.write("      vertex   {} {} {}\n".format(triangle[9], triangle[10], triangle[11]))
            stl.write("    endloop\n")
            stl.write("  endfacet\n")

        stl.write("endsolid\n")

if __name__ == "__main__":
    main()