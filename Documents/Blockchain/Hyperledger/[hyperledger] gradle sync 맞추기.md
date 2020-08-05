# [hyperledger] gradle sync 맞추기

https://stackoverflow.com/questions/57217224/gradle-compile-failed-could-not-find-com-github-everit-org-json-schemaorg-ever



Build 하려고 하니 json-schema 때문에 build가 안된다



-> build.gradle에 아래 코드를 추가한다.

```
repositories {
    mavenLocal()
    mavenCentral()
    maven {
        url "https://repository.mulesoft.org/nexus/content/repositories/public/"
    }
}
```

