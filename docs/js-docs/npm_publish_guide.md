# Guide: Republish JavaScript Package (npm)

Follow these steps to update and republish the JavaScript package after making new changes.

## 1. Update Version in package.json:

Open `js-package/package.json` and increment the version number. Update the "version" field:

```json
{
    "name": "banga",
    "version": "X.Y.Z",  // Increment version number
    // ... other fields ...
}
```

## 2. Create a New Version Tag in Git:
Commit your changes and create a new version tag in Git:

```bash
git add .
git commit -m "Describe your changes"
git tag vX.Y.Z
git push origin vX.Y.Z
```

## 3. Build and Package:
Build and package your JavaScript code:

```bash
cd js-package
npm pack
```

This will create a tarball file in the format banga-X.Y.Z.tgz.

### 4. Publish to npm:
Publish the new version to npm:

```bash
npm publish --access public
```
Now, your updated package is published on npm with the new version.

Remember to update any projects using this package to the latest version.