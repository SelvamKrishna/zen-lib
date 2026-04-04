# TODO

## Math

**Vector**

- [x] vec2, vec3, vec4
- [x] Operations:
  - [x] Add, Subtract
  - [x] Scalar multiply/divide
  - [x] Dot product
  - [x] Cross product
- [x] Utilities:
  - [x] Length / Length squared
  - [x] Normalize
  - [x] Distance
- [x] Advanced:
  - [x] Angle between vectors
  - [x] Reflect
  - [x] Project
  - [x] Refraction
  - [ ] 3D rotations (axis, Euler)
  - [ ] Homogeneous coordinates (vec4)

**Matrix**

- [ ] mat2, mat3, mat4
- [ ] Basic operations:
  - [ ] matrix multiplication
  - [ ] matrix × vector
  - [ ] transpose
- [ ] Determinant (at least mat3/mat4)
- [ ] Inverse (start with mat4)
- [ ] Transform matrices:
  - [ ] translation
  - [ ] rotation (2D + 3D axes)
  - [ ] scaling
- [ ] Projection:
  - [ ] orthographic
  - [ ] perspective

**Quaternion**

- [ ] quaternion struct
- [ ] normalize
- [ ] multiplication
- [ ] conjugate / inverse
- [ ] conversions:
  - [ ] axis-angle ↔ quaternion
  - [ ] Euler ↔ quaternion
- [ ] rotate vector using quaternion
- [ ] interpolation:
  - [ ] lerp
  - [ ] slerp

**Interpolation**

- [x] linear interpolation
- [x] clamped linear interpolation
- [x] smooth step
- [x] smoother step
- [ ] inverse lerp(a, b, v)
- [ ] remap
- [x] Vector versions of lerp
- [x] Angle-aware lerp (wrap-safe)

**Geometry Primitives**

- [ ] 2D
  - [ ] AABB
  - [ ] Circle
  - [ ] Ray2D
  - [ ] Segment2D
- [ ] 3D
  - [ ] AABB3
  - [ ] Sphere
  - [ ] Ray
  - [ ] Plane

**Collision & Intersection**

- [ ] Point tests:
  - [ ] point in AABB
  - [ ] point in circle
- [ ] Shape intersections:
  - [ ] AABB vs AABB
  - [ ] circle vs circle
- [ ] Raycasting:
  - [ ] ray vs AABB
  - [ ] ray vs plane
  - [ ] ray vs sphere
- [ ] Segment tests:
  - [ ] segment vs segment
- [ ] Distance / closest point:
  - [ ] point → line
  - [ ] point → AABB

**Easing / Animation Curves**

- [ ] Ease-in / Ease-out / Ease-in-out
- [ ] Quadratic, Cubic, Exponential
- [ ] Bounce
- [ ] Elastic

**Random Utilities**

- [ ] Random within range
- [ ] Random unit vector (2D/3D)
- [ ] Random direction
- [ ] Seeded RNG support
- [ ] Distribution:
  - [ ] Uniform
  - [ ] Weighted
  - [ ] Normal

**Noise**

- [ ] Value noise
- [ ] Perlin noise
- [ ] Simplex noise
