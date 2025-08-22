terraform {
  cloud {

    organization = "frankfolabi"

    workspaces {
      name = "jenkins"
    }
  }
}