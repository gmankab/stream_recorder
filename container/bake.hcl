group "default" {
  targets = ["amd64", "arm64", "riscv64"]
}

target "amd64" {
  dockerfile = "other.Containerfile"
  platforms = ["linux/amd64"]
  tags = [
    "quay.io/gmanka/stream_recorder:latest",
    "docker.io/gmanka/stream_recorder:latest",
    "ghcr.io/gmankab/stream_recorder:latest"
  ]
}

target "arm64" {
  dockerfile = "other.Containerfile"
  platforms = ["linux/arm64"]
  tags = [
    "quay.io/gmanka/stream_recorder:latest",
    "docker.io/gmanka/stream_recorder:latest",
    "ghcr.io/gmankab/stream_recorder:latest"
  ]
}

target "riscv64" {
  dockerfile = "riscv.Containerfile"
  platforms = ["linux/riscv64"]
  tags = [
    "quay.io/gmanka/stream_recorder:latest",
    "docker.io/gmanka/stream_recorder:latest",
    "ghcr.io/gmankab/stream_recorder:latest"
  ]
}

